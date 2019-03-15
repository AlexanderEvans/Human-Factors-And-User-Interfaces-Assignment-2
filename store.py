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
import imageframe
import productframe
import productrow
import productcanvas
import scrollview
import payment

#additional module imports

#make a menubar
def makeMenu(master):
    menubar = tk.Menu(master = master)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=master.quit)

    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Clear", command=popups.donothing)
    
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About...", command=popups.aboutPage)
    
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Edit", menu=editmenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    return menubar
    


array = []

#Create "top level" window
root = tk.Tk()

#change window title
root.title("Font Shop")
#main code goes here:

#add menubar
root.config(menu=makeMenu(root))

myFrame = tk.Frame(root)

scrollviewFrame = scrollview.VerticalScrolledFrame(myFrame)
arrary = productcanvas.makeProducts(scrollviewFrame)
#scrollviewFrame.grid(row = 0, column=0,  sticky='new')

##add scrollable region
#myCanvas = productcanvas.ProductCanvas(root, scrollregion=(0,0,100,10000), height=400, width=200)
#myScrollbar = ttk.Scrollbar(root, command=myCanvas.yview)
#myCanvas.config(yscrollcommand = myScrollbar.set)
#myCanvas.grid(row = 0, column = 0, sticky = 'nes')
#myScrollbar.grid(row = 0, column = 1, sticky = 'nes')
#
#
#
##figure out how to add rows to a canvas
##makeProducts(myCanvas)
#myCanvas.configure(yscrollincrement='2')
#
#myCanvas.grid_rowconfigure(2, weight=1)
#myCanvas.grid_columnconfigure(2, weight=1)
#

#myImg = PhotoImage(file="myPath")
#testLabelImage = ttk.Label(root, myImg)
#testLabelImage.pack(side = 'left')

##handle scroll inputs
#def rollWheel(event):
#    direction = 0
#    if event.num == 5 or event.delta == -120:
#     direction = 1
#    if event.num == 4 or event.delta == 120:
#     direction = -1
#    event.widget.yview_scroll(direction, UNITS)
#
##bind button event functions to the scrollable region(I don't really know exactly how this is working...)
#myCanvas.bind('<MouseWheel>', lambda event: rollWheel(event))
#myCanvas.bind('<Button-4>', lambda event: rollWheel(event))
#myCanvas.bind('<Button-5>', lambda event: rollWheel(event))
#
#myCanvas.focus_set()

reciept = ""

newWindow = None


        
def bumpTotal(product):
    return (float(product.spinBox.get()) * product.price)

def buildStringFromRowProduct(product):
    myStr = ""
    varient = ""
    if product.buttonGroup==0:
        varient=" - Bold"
    elif  product.buttonGroup==1:
        varient=" - Italic"
    elif  product.buttonGroup==2:
        varient=" - Underlined"
    
    myStr += ( repr(product.spinBox.get()) + product.itemNameAndPriceString + varient)
    myStr += '\n'
    return myStr

def validateRow(row):
    flag = False
    myStr = ""
    total = 0
    print("Left: "+ repr(row.leftProduct.checkboxState.get()) + " : " + repr(int(float(row.leftProduct.spinBox.get()))==0))
    print("Center: "+ repr(row.centerProduct.checkboxState.get()) + " : " + repr(int(float(row.centerProduct.spinBox.get()))==0))
    print("Right: "+ repr(row.rightProduct.checkboxState.get()) + " : " + repr(int(float(row.rightProduct.spinBox.get()))==0))
    if row.leftProduct.checkboxState.get() and (int(float(row.leftProduct.spinBox.get()))==0):
        flag=True
    elif row.leftProduct.checkboxState.get():
        myStr += buildStringFromRowProduct(row.leftProduct)
        total += bumpTotal(row.leftProduct)
    if row.centerProduct.checkboxState.get() and (int(float(row.centerProduct.spinBox.get()))==0):
        flag=True
    elif row.centerProduct.checkboxState.get():
        myStr += buildStringFromRowProduct(row.centerProduct)
        total += bumpTotal(row.centerProduct)
    if row.rightProduct.checkboxState.get() and (int(float(row.rightProduct.spinBox.get()))==0):
        flag=True
    elif row.rightProduct.checkboxState.get():
        myStr += buildStringFromRowProduct(row.rightProduct)
        total += bumpTotal(row.rightProduct)
    reciept = myStr
    return flag, total

def nextPage():
    total = 0
    error = False
    for row in arrary:
        catch = False
        catch, total = validateRow(row)
        if catch:
            error=True

    ignoreError = True
    if error:
        ignoreError = popups.invalidInputWarning()

    if ignoreError:
        newWindow = payment.Payment(None, reciept, total)

        

testVar = tk.Button(myFrame, command = nextPage, text = "Go to Checkout ->")
testVar.pack(side = 'bottom')
scrollviewFrame.pack(side = 'top')
#testVar.grid(row=1, column=0, sticky='wse')

myFrame.pack(fill = 'both', expand = 1)

#Start the event loop
root.mainloop();

#def getItems():
#    rtnVal = StringVar()
#    for val in myCanvas.children:
#        for productFrame in val.children:
#            rtnVal += (productFrame.checkboxState + "\n")
#            rtnVal += (productFrame.buttonGroup + "\n")
#    return rtnVal
