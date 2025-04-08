import tkinter as tk
from PIL import Image, ImageTk


class Gui():
    def __init__(self, room):
        self.room = None
        self.root = tk.Tk()
        self.init_window()
        self.create_game_frame()

    def init_window(self):
        self.root.title("Dracula's Castle")
        self.game_frame = tk.Frame(self.root, width=self.screensize[0], height=(self.screensize[1]))
    
    def create_game_frame(self):
        # will call Rooms class to create Gui frames
        pass
       
    def update_room(self):
        # change room variable to next room name
        # shut down previous frame
        # call next frame to be created
        pass
    
class Rooms():
    # has 7 kinds of frames for different stages of the game
    # labels for each room explaining the situation will be referenced through a JSON file for specific monster and room information
    def __init__(self, room):
        self.room = room

    def castle_screen(self):
        # title page for game
        pass

    def dead_room(self):
        # where you are sent when you die
        # has text based on what room you were in last and what monster killed you
        pass

    def instruction_room(self):
        # first place you are sent from starter page
        # has a start button and an exit button
        pass

    def monster_room1(self):
        # where a random monster is
        # gives you three buttons to choose from
        pass

    def monster_room2(self):
        # random monster of the other two monsters
        pass

    def monster_room3(self):
        # last monster
        pass

    def monster_room4(self):
        # where a Dracula is 
        pass

class Actions():
    # will be what the buttons do in gui frames
    def __init__(self):
        pass

    def attack(self):
        # 50% chance of attacking and suriving or dying
        pass

    def escape(self):
        # change variable to escape
        # change room
        pass

    def die(self):
        # send to dead room
        pass
    
    def go(self):
        # move to next frame
        pass
    

    


        

def main():
    my_display = Gui()
    my_display.root.mainloop()

if __name__ == "__main__":
    main()
