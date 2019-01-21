# Part of the core python language
from tkinter import *
# Binding a function to a widget

""" Add a basic window with close sign, minimize, and maximize (Main Window)"""
root = Tk()

##############
# METHOD ONE #
##############
""" 
def printName():
    print("Your waifu sucks!")

button_1 = Button(root, text="A message for you.", command=printName)
button_1.pack()
 """
##############
# METHOD TWO #
##############


def printName(event):
    print("Your waifu sucks!")


button_1 = Button(root, text="A message for you.")
""" <Button-1> is the left mouse click """
button_1.bind("<Button-1>", printName)
button_1.pack()

""" Enable the Main Window to stay on the screen """
root.mainloop()
