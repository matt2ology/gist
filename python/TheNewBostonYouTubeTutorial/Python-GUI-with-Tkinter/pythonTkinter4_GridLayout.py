# Part of the core python language
from tkinter import *

""" Add a basic window with close sign, minimize, and maximize (Main Window)"""
root = Tk()

userNamePrompt = label(root, Text="Enter Username")
passwordPrompt = label(root, Text="Enter Password")

userNameField = entry(root)
passwordField = entry(root)

userNamePrompt.grid(row=0)
passwordPrompt.grid(row=1)

userNameField.grid(row=0,column=1)
passwordPrompt.grid(row=1,column=1)

""" Enable the Main Window to stay on the screen """
root.mainloop()