# Part of the core python language
from tkinter import *

""" Add a basic window with close sign, minimize, and maximize (Main Window) """
root = Tk()

""" Make an invisible container and it's going to go in the main window (the root) """ 
topFrame = Frame(root)

""" Place it somewhere in our Main Window """
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

""" Create widgets """
buttonSubmit = Button(topFrame, text="Submit", fg="green")
buttonStop = Button(topFrame, text="Stop", fg="red")
buttonCaution = Button(topFrame, text="Caution", fg="orange")
buttonIntel = Button(bottomFrame, text="Intel", fg="Blue",bg="orange")

""" Display widgets """
buttonSubmit.pack(side=LEFT)
buttonStop.pack(side=RIGHT)
buttonCaution.pack(side=LEFT)
buttonIntel.pack(side=BOTTOM)

""" Enable the Main Window to stay on the screen """
root.mainloop()