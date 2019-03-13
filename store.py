#**********************************************************************
#****      Student: Alexander Evans                                ****
#****        Class: Human Factors and User Interfaces              ****
#****   Instructor: Gamradt                                        ****
#****   Assignment: 2                                              ****
#****     Due Date: 2/9/2019                                       ****
#**********************************************************************
#****  Description:                                                ****
#**********************************************************************
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import popups
import productrow
#additional module imports

#make a menubar
def makeMenu(parent):
    menubar = tk.Frame(parent)
    menubar.pack(side = 'top', fill = 'x')
    btnFile = tk.Menubutton(menubar, text = 'File', underline = 0)
    btnFile.pack(side='left')
    btnFile = tk.Menubutton(menubar, text = 'Edit', underline = 0)
    btnFile.pack(side='left')
    btnFile = tk.Menubutton(menubar, text = 'Help', underline = 0)
    btnFile.pack(side='left')
    

#hardcoded for now, make a row of 3 pruducts.
def makeProducts(parent):
    #make product rows
    productrow.ProductRow(parent = parent, fontNames ={'L','C','R'})
    productrow.ProductRow(parent = parent, fontNames ={'L','C','R'})
    productrow.ProductRow(parent = parent, fontNames ={'L','C','R'})


#Create "top level" window
root = tk.Tk()

#main code goes here:
#myLabel = tk.Label(root, text="Hello World")

#change window title
root.title("Font Shop")

#add menubar
makeMenu(root)

#add scrollable region
myCanvas = tk.Canvas(root, scrollregion=(0,0,500,500), height=200, width=200)
myScrollbar = ttk.Scrollbar(root, command=myCanvas.yview)
myCanvas.config(yscrollcommand = myScrollbar.set)
myScrollbar.pack(side='right', fill = 'y')


#figure out how to add rows to a canvas
#makeProducts(myCanvas)
makeProducts(myCanvas)

myCanvas.pack(fill='both', expand=1)
myCanvas.configure(yscrollincrement='2')


#myImg = PhotoImage(file="myPath")
#testLabelImage = ttk.Label(root, myImg)
#testLabelImage.pack(side = 'left')

#handle scroll inputs
def rollWheel(event):
    direction = 0
    if event.num == 5 or event.delta == -120:
     direction = 1
    if event.num == 4 or event.delta == 120:
     direction = -1
    event.widget.yview_scroll(direction, UNITS)

#bind button event functions to the scrollable region(I don't really know exactly how this is working...)
myCanvas.bind('<MouseWheel>', lambda event: rollWheel(event))
myCanvas.bind('<Button-4>', lambda event: rollWheel(event))
myCanvas.bind('<Button-5>', lambda event: rollWheel(event))

myCanvas.focus_set()

#Start the event loop
root.mainloop();

