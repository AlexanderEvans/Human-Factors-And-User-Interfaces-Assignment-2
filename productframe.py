import tkinter as tk
from tkinter import ttk
import imageframe

class ProductFrame(tk.Frame):
    def __init__(self, parent = None, text = "Default Text: ", price = 1.99, height = 100, width = 100):
        super().__init__(parent)
        self.parent=parent
        self.text = text
        self.price = price
        self.create_widgets()

    def create_widgets(self):
        #line one of frame:
        self.checkboxState = tk.BooleanVar()
        self.checkbox = ttk.Checkbutton(self, variable = self.checkboxState)
        self.itemNameAndPriceString = (self.text + repr(self.price))
        self.itemNameAndPrice = ttk.Label(self, text = self.itemNameAndPriceString)

        self.var = tk.StringVar()
        self.var.set("0")
        self.spinBox = ttk.Spinbox(self, from_ = 0, to = 9999, textvariable = self.var)

        #line 2
        self.buttonGroup = tk.IntVar()
        self.radioButtonBold = ttk.Radiobutton(self, text = "Bold", variable = self.buttonGroup, value = 0)
        self.radioButtonItalic = ttk.Radiobutton(self, text = "Italic", variable = self.buttonGroup, value = 1)
        self.radioButtonUnderlined = ttk.Radiobutton(self, text = "Underlined", variable = self.buttonGroup, value = 2)
        
        #line 3
        self.productImage = imageframe.ImageFrame(self)
        self.productImage.grid(row=2,column=0, columnspan = 3)

        self.checkbox.grid(row=0,column=0)
        self.itemNameAndPrice.grid(row=0,column=1)
        self.spinBox.grid(row=0,column=2)
        self.radioButtonBold.grid(row=1,column=0)
        self.radioButtonItalic.grid(row=1,column=1)
        self.radioButtonUnderlined.grid(row=1,column=2)