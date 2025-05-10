import tkinter as tk
from PIL import Image, ImageTk
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
        self.last_button_pressed = None
        self.root = tk.Tk()
        self.init_window()

    def init_window(self):
        ###creates the window for the app
        self.root.title("Dracula's Castle")
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack(fill="both", expand=True)

        self.title_page = tk.Frame(self.game_frame)
        self.room_page = tk.Frame(self.game_frame)
        self.result_page = tk.Frame(self.game_frame)
        ### fits the different frames into a larger frame that change size based on need
        for frame in (self.title_page, self.room_page, self.result_page):
            frame.grid(row=0, column=0, sticky="nsew")
        ### add buttons and labels to the different frames 
        self.setup_title_page()
        self.setup_room_page()
        self.setup_result_page()
        ### opens the title page
        self.show_page(self.title_page)

    def setup_title_page(self
        
        title_label = tk.Label(self.title_page, text="Welcome to Dracula's Castle!!").pack(pady=10)
        info_label = tk.Label(self.title_page, text=text_dictionary["instructions"]).pack()
        # title_label.place(x=self.screensize[0]/2-70, y=(self.screensize[1]/2))
    
        ### uses lambda command so button choice called
        start_button = tk.Button(self.title_page, text="Start", command=lambda: self.button_choice(page="room")).pack()
        # start_button.place(x=(self.screensize[0]/2-10), y=(5*(self.screensize[1])/6))

        quit_button = tk.Button(self.title_page, text="Quit", command=self.root.destroy).pack()
        # quit_button.place(x=(self.screensize[0]/2-20), y=(5*(self.screensize[1])/6))

    def setup_room_page(self):
        
        self.room_label = tk.Label(self.room_page, text="")
        self.room_label.pack(pady=10)
        # label1.place(x=self.screensize[0]/2-70, y=(self.screensize[1]/2))
        
        ### passes the button choice method which room the button is in and which button was pressed
        self.attack_button = tk.Button(self.room_page, text="", command=lambda: self.button_choice(page="room",button="attack"))
        self.attack_button.pack()
        # attack_button.place(x=(self.screensize[0]/2-70), y=(5*(self.screensize[1])/6))

        self.escape_button = tk.Button(self.room_page, text="", command=lambda: self.button_choice(page="room",button="escape"))
        self.escape_button.pack()
        # escape_button.place(x=(self.screensize[0]/2-40), y=(5*(self.screensize[1])/6))

        self.die_button = tk.Button(self.room_page, text="", command=lambda: self.button_choice(page="room",button="die"))
        self.die_button.pack()
        # die_button.place(x=(self.screensize[0]/2-10), y=(5*(self.screensize[1])/6))

        quit_button = tk.Button(self.room_page, text="Quit", command=self.root.destroy).pack()
        # quit_button.place(x=(self.screensize[0]/2-20), y=(5*(self.screensize[1])/6))

    def setup_result_page(self):
        
        self.result_label = tk.Label(self.result_page, text="")
        self.result_label.pack(pady=10)
        # label1.place(x=self.screensize[0]/2-70, y=(self.screensize[1]/2))

        self.next_button = tk.Button(self.result_page, text="Continue", command=lambda: self.button_choice(page="room"))
        self.next_button.pack()
        # next_button.place(x=(self.screensize[0]/2-10), y=(5*(self.screensize[1])/6))

        quit_button = tk.Button(self.result_page, text="Quit", command=self.root.destroy).pack()
        # quit_button.place(x=(self.screensize[0]/2-20), y=(5*(self.screensize[1])/6))
    ### shows the called frame
    def show_page(self, frame):
        frame.tkraise()
        
    ### decides whether you die when you press attack option
    def attack(self):
        outcome_list = ["attack/survive", "attack/die"]
        outcome = random.choice(outcome_list)

        return outcome
    ### changes the labels and button labels depending on what room you are in and what button you press
    def button_choice(self, page=None, button=None):
        ### makes consequence
        if button == "attack":
            consequence = self.attack()
        else:
            consequence = button
        ### changes the room when you choose an option but not when you press continue
        if button != None:
            self.room += 1
        ### sends you home if you die
        if button == "die":
            self.next_button.config(text="Go Home", command= lambda: self.show_page(self.title_page))
            self.room -= self.room - 1
        ### sets labels for everything based on current conditions
        if self.room<=3:
            self.last_button_pressed = button
            self.room_label.config(text=self.update_text(page, button))
            self.attack_button.config(text=self.update_text(page, button="attack"))
            self.escape_button.config(text=self.update_text(page, button="escape"))
            self.die_button.config(text=self.update_text(page, button="die"))
            self.result_label.config(text=self.update_text(page, button, consequence=consequence))
        else:
            ### sets labels on draculas room (not randomized monster)
            self.last_button_pressed = button
            self.room_label.config(text=self.update_text(page, button, dracula=True))
            self.attack_button.config(text=self.update_text(page, button="attack", dracula=True))
            self.escape_button.config(text=self.update_text(page, button="escape", dracula=True))
            self.die_button.config(text=self.update_text(page, button="die", dracula=True))
            self.result_label.config(text=self.update_text(page, button, consequence=consequence, dracula=True))
            self.next_button.config(text="Go Home", command= lambda: self.show_page(self.title_page))
            self.room -= 3
        ### dictates next room
        if self.last_button_pressed == None:
            self.show_page(self.room_page)
        else:
            self.show_page(self.result_page)
    ### finds specific label based on current contidions
    def update_text(self, page=None, button=None, consequence=None, dracula=None):
        if page != None and button != None and consequence == None and dracula == None:
            text = text_dictionary["buttons"][button][f"room{self.room}"]
        if page != None and button != None and consequence != None and dracula == None:
            text = text_dictionary["action consequences"][f"room{self.room}"][f"{self.monster}"][consequence]
        if page != None and button == None and consequence == None and dracula == None:
            text = text_dictionary["room introduction"][f"{self.monster_randomizer()}"][f"room{self.room}"]
        if page != None and button != None and consequence == None and dracula:
            text = text_dictionary["buttons"][button][f"room{self.room}"]
        if page != None and button != None and consequence != None and dracula:
            text = text_dictionary["action consequences"]["dracula"][consequence]
        if page != None and button == None and consequence == None and dracula:
            text = text_dictionary["room introduction"][f"room{self.room}"]

        return text
    #randomizes monster for first 3 rooms
    def monster_randomizer(self):
        dead_monsters = []
        monsters = ["wolf", "zombie", "spider"]
        if self.monster != None:
            dead_monsters.append(self.monster)
            for i in range(len(dead_monsters)):
                monsters.remove(dead_monsters[i])
        monster = random.choice(monsters)
        self.monster = monster

        return monster

def main():
    my_display = DraculaApp()
    my_display.root.mainloop()

if __name__ == "__main__":
    main()
