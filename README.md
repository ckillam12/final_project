 # final_project
My project will be a game where you are taken into Dracula's castle going from room to room fighting monsters.
At each room there is a monster that you will have to deal with in some way. 
The program will first load a GUI and begin a sequence of frames with the first printing an explanation of the user's predicament in Dracula's castle, and then instructions on how to play the game and escape the castle. 
The program will then put the user into a room where a monster will be. 
The monster will be either a wolf, zombie, or spider and will be randomly chosen for each room besides the last room where Dracula is.
The program will give a list of a few options, and depending on what the user inputs, will allow them to escape the monster, kill the monster, or be killed. 
After going through the rooms, you will finally fight Dracula and either be killed or successfully escape the castle.

The program will work through a Tkinter GUI class that will change labels and buttons depending on the "room" the player is in.
- Gui class functions:
 Will create frames necessary for the game to run and use a show_page function to bring the needed frame onto the screen
- Rooms class functions:
 Button choice be called when a button is pressed and will be passed the type of button pressed and which room the button was pressed in
- Actions class functions
 Attack function will choose whether or not you die
- Labels:
 Text will be organized in a JSON file for each action, room, and monster combination and labels will be updated showing each rooms description of the users situation

