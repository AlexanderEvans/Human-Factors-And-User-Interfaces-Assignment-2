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
import productframe
import productrow
import productcanvas

#additional module imports

def donothing():
     messagebox.showinfo(title = 'About', message = 'not implemented yet')
     
def aboutPage():
    messagebox.showinfo(title = 'About', message = 'This is the Font Shop!  Welcome to the Font Shop!  Please enjoy, the Font Shop!')

#make a menubar
def makeMenu(master):
    menubar = tk.Menu(master = master)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=master.quit)

    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Clear", command=donothing)
    
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About...", command=aboutPage)
    
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Edit", menu=editmenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    return menubar
    




#Create "top level" window
root = tk.Tk()

#change window title
root.title("Font Shop")

#main code goes here:

#add menubar
root.config(menu=makeMenu(root))


#add scrollable region
myCanvas = productcanvas.ProductCanvas(root, scrollregion=(0,0,500,5500), height=200, width=200)
myScrollbar = ttk.Scrollbar(root, command=myCanvas.yview)
myCanvas.config(yscrollcommand = myScrollbar.set)
myScrollbar.pack(side='right', fill = 'y')


#figure out how to add rows to a canvas
#makeProducts(myCanvas)
myCanvas.pack(fill='both', expand=1)
myCanvas.configure(yscrollincrement='2')

myCanvas.grid_rowconfigure(2, weight=1)
myCanvas.grid_columnconfigure(2, weight=1)



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

testVar = productframe.ProductFrame(root, "emerge test", 9.99)
testVar.pack();

#Start the event loop
root.mainloop();

#def getItems():
#    rtnVal = StringVar()
#    for val in myCanvas.children:
#        for productFrame in val.children:
#            rtnVal += (productFrame.checkboxState + "\n")
#            rtnVal += (productFrame.buttonGroup + "\n")
#    return rtnVal
