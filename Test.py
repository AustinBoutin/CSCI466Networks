from tkinter import *
root = Tk()
buttons = []

def set_buttons():
    for i in range(8):
        buttons.append([])
        for j in range(8):
            buttons[i].append(ttk.Button(text='3'))
            buttons[i][j].configure(command=com)
            buttons[i][j].grid(row=i, column=j, sticky="nsew")

def com():
    print (3)

set_buttons()
root.mainloop()
