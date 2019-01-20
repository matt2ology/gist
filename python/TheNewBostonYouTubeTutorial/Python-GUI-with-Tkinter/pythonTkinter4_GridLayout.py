# Part of the core python language
from tkinter import *

""" Add a basic window with close sign, minimize, and maximize (Main Window)"""
root = Tk()

label_1 = Label(root, Text="Enter Username") """ userNamePrompt """
label_2= Label(root, Text="Enter Password") """ passwordPrompt """

entry_1 = Entry(root) """ userNameField """
entry_2 = Entry(root) """ passwordField """

label_1.grid(row=0) """ userNamePrompt """
label_2.grid(row=1) """ passwordPrompt """

entry_1.grid(row=0,column=1) """ userNameField """
entry_2.grid(row=1,column=1) """ passwordPrompt """

""" Enable the Main Window to stay on the screen """
root.mainloop()
