import tkinter as tk
from PIL import Image, ImageTk

class Display():
    screensize = (800,600)
    image_handle = "C:/Users/ckill/OneDrive/Documents/runner.gif"
    def __init__(self):
        self.image = None
        self.photo = None
        self.image_x = 0
        self.image_y = 0
        self.image_width = 0
        self.image_height = 0
        self.movement_speed = 0
        self.root = tk.Tk()
        self.init_window()
        self.create_game_frame()
        self.create_interface_frame() 

    def init_window(self):
        self.root.title("Dracula's Casle")
        self.game_frame = tk.Frame(self.root, width=self.screensize[0], height=((5*self.screensize[1])//6))
        self.game_frame.grid(row=0)

        self.interface_frame = tk.Frame(self.root, width=self.screensize[0], height=(self.screensize[1]//6))
        self.interface_frame.grid(row=1)








def main():

if __name__ == "__main__":
    main()