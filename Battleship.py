import sys
from tkinter import *

class Battleship:

    def get_tile_color(self, tile):
        return{
            'C' : "#FF9232",
            'B' : "#FFEC23",
            'R' : "#91FF23",
            'S' : "#22F9C4",
            'D' : '#2226F9'
            }.get(tile, "#FFF")

    def fire(self, x_entry, y_entry):
        x_cord = x_entry.get()
        y_cord = y_entry.get()
        print(x_cord + ", " + y_cord)

    def __init__(self, master):

        port = sys.argv[0]
        #boardFile = sys.argv[1]
        testboard = [['C','C','C','C','C','_','_','_','_','_'],
                     ['B','B','B','B','_','_','_','_','_','_'],
                     ['R','R','R','_','_','_','_','_','_','_'],
                     ['S','S','S','_','_','_','_','_','_','_'],
                     ['D','_','_','_','_','_','_','_','_','_'],
                     ['D','_','_','_','_','_','_','_','_','_'],
                     ['_','_','_','_','_','_','_','_','_','_'],
                     ['_','_','_','_','_','_','_','_','_','_'],
                     ['_','_','_','_','_','_','_','_','_','_'],
                     ['_','_','_','_','_','_','_','_','_','_']]


        frame = Frame(master)
        frame.pack()

        player_grid = Frame(frame)
        player_grid.grid(row=0, column=0, padx = 25, pady = 25)

        for y in range(0, 10):
            subframe = Frame(player_grid)
            subframe.grid(row=y)
            for x in range(0, 10):
                button_color = self.get_tile_color(testboard[y][x])
                self.button = Button(subframe, height = 1, width = 2, bg=button_color, state=DISABLED)
                self.button.grid(row=y, column=x)

        opponent_grid = Frame(frame)
        opponent_grid.grid(row=0, column=1, padx=25, pady=25)
        
        for y in range(0, 10):
            subframe = Frame(opponent_grid)
            subframe.grid(row=y)
            for x in range(0, 10):
                self.button = Button(subframe, width = 2, height = 1, bg="#fff", state=DISABLED)
                self.button.grid(row=y, column=x)

        input_frame = Frame(frame)
        input_frame.grid(row = 1, column = 0, columnspan = 2)
        
        l = Label(input_frame, text="X:")
        l.grid(row=0, column=0)

        x_entry = Entry(input_frame)
        x_entry.grid(row=0, column=1, pady=5)

        l = Label(input_frame, text="Y:")
        l.grid(row=1, column=0)

        y_entry = Entry(input_frame)
        y_entry.grid(row=1, column=1)

        fire_button = Button(input_frame, text="FIRE!", command= lambda: self.fire(x_entry, y_entry))
        fire_button.grid(row=3, column=1, pady=5)

root = Tk()

app = Battleship(root)

root.mainloop()
root.destroy
