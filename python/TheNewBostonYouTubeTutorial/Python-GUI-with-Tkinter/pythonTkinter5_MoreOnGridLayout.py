# Part of the core python language
from tkinter import *

""" Add a basic window with close sign, minimize, and maximize (Main Window)"""
root = Tk()

userNamePrompt = Label(root, text="Username")
passwordPrompt = Label(root, text="Password")

userNameField = Entry(root)
passwordField = Entry(root)

""" Sticky=E keeps text right aligned with respective cardinal directions """
userNamePrompt.grid(row=0, sticky=E)
passwordPrompt.grid(row=1, sticky=E)

userNameField.grid(row=0, column=1)
passwordField.grid(row=1, column=1)

""" Takes the center of the two spanned column """
checkBox = Checkbutton(root, text="Keep me signed in.")
checkBox.grid(columnspan=2)

""" Enable the Main Window to stay on the screen """
root.mainloop()
