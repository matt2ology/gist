# Part of the core python language
from tkinter import *

""" Add a basic window with close sign, minimize, and maximize (Main Window)"""
root = Tk()

userNamePrompt = Label(root, text="Enter Username")
passwordPrompt = Label(root, text="Enter Password")

userNameField = Entry(root)
passwordField = Entry(root)

label_1.grid(row=0) """ userNamePrompt """
label_2.grid(row=1) """ passwordPrompt """

userNameField.grid(row=0, column=1)
passwordField.grid(row=1, column=1)

""" Enable the Main Window to stay on the screen """
root.mainloop()
