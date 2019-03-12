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
#import productframe
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
myCanvas.pack(side='left')
myScrollbar.pack(side='right', fill='y')
myCanvas.configure(yscrollincrement='2')

#handle scroll inputs
def rollWheel(event):
    direction = 0
    if event.num == 5 or event.delta == -120:
     direction = 1
    if event.num == 4 or event.delta == 120:
     direction = -1
    event.widget.yview_scroll(direction, UNITS)

#bind button event functions to the scrollable region
myCanvas.bind('<MouseWheel>', lambda event: rollWheel(event))
myCanvas.bind('<Button-4>', lambda event: rollWheel(event))
myCanvas.bind('<Button-5>', lambda event: rollWheel(event))

myCanvas.focus_set()

#Start the event loop
root.mainloop();



#hardcoded for now
def makeProducts(parent):
    myStringVarList = {'Bold','Italic','Underline'}
    pOne = ProductFrame(self)
    pOne.__init__(myStringVarList, parent)
    pTwo = ProductFrame(self)
    pTwo.__init__(myStringVarList, parent)
    pThree = ProductFrame(self, )
    pThree.__init__(myStringVarList, parent)

class ProductFrame(tk.Frame):
    def __init__(self, myStringVarList = [], parent = None):
        super().__init__(parent)
        self.parent=parent
        self.pack()
        self.create_widgets()
        self.myStringVarList = myStringVarList

    def create_widgets(self):
        #line one of frame:
        self.checkbox = ttk.Checkbutton(self)
        self.itemNameAndPrice = ttk.Label(self)
        self.spinBox = ttk.Spinbox(self)

        #line 2
        self.buttonGroup = StringVar()
        self.buttonGroup.set(0)
        self.radioButtonOne = ttk.Radiobutton(self, text = myStringVarList[1], variable = buttonGroup, value = 0)#I think array starts at 1 in python???
        self.radioButtonTwo = ttk.Radiobutton(self, text = myStringVarList[2], variable = buttonGroup, value = 1)
        self.radioButtonThree = ttk.Radiobutton(self, text = myStringVarList[3], variable = buttonGroup, value = 2)
        
        #line 3
        self.productImage = tk.Image()


        self.checkbox.pack(side = 'left')
        self.itemNameAndPrice.pack(side = 'top')
        self.spinBox.pack(side = 'right')
        self.radioButtonOne.pack(side = 'left')
        self.radioButtonTwo.pack(side = 'top')
        self.radioButtonThree.pack(side = 'right')
        self.productImage.pack(top)


