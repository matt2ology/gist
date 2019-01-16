# Part of the core python language
from tkinter import *

""" Add a basic window with close sign, minimize, and maximize (Main Window)"""
root = Tk()
""" Place label in root (the Main Window/the parent) """
intel = Label(root,text="matt2ology", fg="blue", bg="orange")
""" Fill as large as the text it contains """
intel.pack()

blackPink = Label(root,text="In your area!", fg="black", bg="pink")
""" Fill in Main WIndow as wide as the X value of the parent """
blackPink.pack(fill=X)

houseOfPain = Label(root,text="Pack it up, pack it in.", fg="white", bg="black")
houseOfPain.pack(side=LEFT, fill=Y)

""" Enable the Main Window to stay on the screen """
root.mainloop()
