import tkinter as tk
import json
import random

with open("label_texts.JSON") as file_handle:
    json_string = file_handle.read()
text_dictionary = json.loads(json_string)

class DraculaApp():
    screensize = (800,600)
    def __init__(self):
        self.room = 1
        self.monster = None
        self.used_monsters = []
        self.last_button_pressed = None
        self.last_button_checker = 0 
        self.root = tk.Tk()
        self.init_window()

    def init_window(self):
        ### will open game pages
        self.root.title("Dracula's Castle")
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack(fill="both", expand=True)

        self.title_page = tk.Frame(self.game_frame)
        self.room_page = tk.Frame(self.game_frame)
        self.result_page = tk.Frame(self.game_frame)

        for frame in (self.title_page, self.room_page, self.result_page):
            frame.grid(row=0, column=0, sticky="nsew")

        self.setup_title_page()
        self.setup_room_page()
        self.setup_result_page()

        self.show_page(self.title_page)

    def setup_title_page(self):
        title_label = tk.Label(self.title_page, text="Welcome to Dracula's Castle!!").pack(pady=10)
        info_label = tk.Label(self.title_page, text=text_dictionary["instructions"]).pack()

        self.start_button = tk.Button(self.title_page, text="Start", command=lambda: self.button_choice(page="room"))
        self.start_button.pack()

        quit_button = tk.Button(self.title_page, text="Quit", command=self.root.destroy).pack()

    def setup_room_page(self):
        
        self.room_label = tk.Label(self.room_page, text="")
        self.room_label.pack(pady=10)

        self.attack_button = tk.Button(self.room_page, text="", command=lambda: self.button_choice(page="room",button="attack"))
        self.attack_button.pack()

        self.escape_button = tk.Button(self.room_page, text="", command=lambda: self.button_choice(page="room",button="escape"))
        self.escape_button.pack()

        self.die_button = tk.Button(self.room_page, text="", command=lambda: self.button_choice(page="room",button="die"))
        self.die_button.pack()

        quit_button = tk.Button(self.room_page, text="Quit", command=self.root.destroy)
        quit_button.pack()

    def setup_result_page(self):
        
        self.result_label = tk.Label(self.result_page, text="")
        self.result_label.pack(pady=10)
    
        self.next_button = tk.Button(self.result_page, text="Continue", command=lambda: self.button_choice(page="room"))
        self.next_button.pack()

        quit_button = tk.Button(self.result_page, text="Quit", command=self.root.destroy)
        quit_button.pack()

    def show_page(self, frame):
        ### brings up called page
        frame.tkraise()

    def attack(self):
        ### chooses outcome of attack choice
        outcome_list = ["attack/survive", "attack/die"]
        outcome = random.choice(outcome_list)

        return outcome

    def button_choice(self, page=None, button=None):
        ### chooses outcome of button choice

        ### update after start and continue buttons
        if button is None and self.room < 4:
            self.monster = self.monster_randomizer()
            self.last_button_pressed = None
            self.room_label.config(text=self.update_text(page, button=None))
            self.attack_button.config(text=self.update_text(page, "attack"))
            self.escape_button.config(text=self.update_text(page, "escape"))
            self.die_button.config(text=self.update_text(page, "die"))
            self.shuffle_buttons()
            self.show_page(self.room_page)
            return
        
        self.last_button_pressed = button
        ### specifies outcome based on button choice
        if button == "attack":
            consequence = self.attack()
        else:
            consequence = button
        ### Go back to home page after death
        if button == "die" or consequence == "attack/die":
            if self.room < 4:
                self.result_label.config(text=self.update_text(page, button, consequence=consequence))
            else:
                self.result_label.config(text=self.update_text(page, button, consequence=consequence, dracula=True))
            self.next_button.config(text="Go Home", command= lambda: self.show_page(self.title_page))
            self.reset_game()
            self.show_page(self.result_page)
            return
        ### update after action buttons
        if self.room < 4:
            self.room_label.config(text=self.update_text(page, button))
            self.attack_button.config(text=self.update_text(page, button="attack"))
            self.escape_button.config(text=self.update_text(page, button="escape"))
            self.die_button.config(text=self.update_text(page, button="die"))
            self.shuffle_buttons()
            self.result_label.config(text=self.update_text(page, button, consequence=consequence))
            self.next_button.config(text="Continue", command=lambda: self.button_choice(page="room"))
            if self.last_button_pressed in ["attack","escape"]:
                self.room += 1
                self.monster = None
            self.show_page(self.result_page)
            return
        ### update for final room
        if self.last_button_checker == 0:
            self.room_label.config(text=self.update_text(page, button=None, dracula=True))
            self.attack_button.config(text=self.update_text(page, button="attack", dracula=True))
            self.escape_button.config(text=self.update_text(page, button="escape", dracula=True))
            self.die_button.config(text=self.update_text(page, button="die", dracula=True))
            self.shuffle_buttons()
            self.last_button_checker = 1
            self.show_page(self.room_page)
            return
        ### update after action button in final room
        else:
            self.result_label.config(text=self.update_text(page, button, consequence=consequence, dracula=True))
            self.next_button.config(text="Go Home", command=lambda: self.show_page(self.title_page))
            self.reset_game()
            self.show_page(self.result_page)
            return

    def update_text(self, page=None, button=None, consequence=None, dracula=None):
        ### gets text from JSON file for specific conditions
        if page != None and button != None and consequence == None and dracula == None:
            text = text_dictionary["buttons"][button][f"room{self.room}"]
        if page != None and button != None and consequence != None and dracula == None:
            text = text_dictionary["action consequences"][f"room{self.room}"][self.monster][consequence]
        if page != None and button == None and consequence == None and dracula == None:
            text = text_dictionary["room introduction"][self.monster][f"room{self.room}"]
        if page != None and button != None and consequence == None and dracula:
            text = text_dictionary["buttons"][button][f"room{self.room}"]
        if page != None and button != None and consequence != None and dracula:
            text = text_dictionary["action consequences"]["dracula"][consequence]
        if page != None and button == None and consequence == None and dracula:
            text = text_dictionary["room introduction"]["dracula"]

        return text

    def monster_randomizer(self):
        ### randomizes monster for each room
        monsters = ["wolf", "zombie", "spider"]
        if len(self.used_monsters) >= len(monsters):
            self.used_monsters = []
        if self.monster != None:
            for used in self.used_monsters:
                if used in monsters:
                    monsters.remove(used)
        monster = random.choice(monsters)
        self.used_monsters.append(monster)
        self.monster = monster

        return monster
    def shuffle_buttons(self):
        ### shuffles the order of the buttons
        button_list = [self.attack_button, self.escape_button, self.die_button]
        for button in button_list:
            button.pack_forget()

        random.shuffle(button_list)
        for button in button_list:
            button.pack()
    
    def reset_game(self):
        ### resets game to original state
        self.room = 1
        self.monster = None
        self.used_monsters = []
        self.last_button_pressed = None
        self.last_button_checker = 0
    
def main():
    my_display = DraculaApp()
    my_display.root.mainloop()

if __name__ == "__main__":
    main()
