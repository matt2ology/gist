# Part of the core python language
from tkinter import *
# Binding a function to a widget

""" Add a basic window with close sign, minimize, and maximize (Main Window)"""
window_1 = Tk(className="window_1")
window_2 = Tk(className="window_2")

##############
# METHOD ONE #
##############


def printName():
    print("Your waifu sucks!")


button_1 = Button(window_1, text="A message for you.", command=printName)
button_1.pack()

##############
# METHOD TWO #
##############


def printName(event):
    print("No, your waifu sucks!")


button_1 = Button(window_2, text="A message for you.")

""" <Button-1> is the left mouse click """
button_1.bind("<Button-1>", printName)
button_1.pack()

""" Enable the Main Window to stay on the screen """
window_1.mainloop()
window_2.mainloop()
