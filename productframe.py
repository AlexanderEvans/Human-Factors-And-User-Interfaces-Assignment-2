import tkinter as tk
from tkinter import ttk

class ProductFrame(tk.Frame):
    def __init__(self, parent = None, text = "Default Text"):
        super().__init__(parent)
        self.parent=parent
        self.pack()
        self.create_widgets()
        self.text = text;

    def create_widgets(self):
        #line one of frame:
        self.checkboxState = tk.BooleanVar()
        self.checkbox = ttk.Checkbutton(self, variable = self.checkboxState)
        self.itemNameAndPrice = ttk.Label(self, text=self.text)
        self.spinBox = ttk.Spinbox(self)

        #line 2
        self.buttonGroup = tk.StringVar()
        self.buttonGroup.set(0)
        self.radioButtonBold = ttk.Radiobutton(self, text = "Bold", variable = buttonGroup, value = 0)
        self.radioButtonItalic = ttk.Radiobutton(self, text = "Italic", variable = buttonGroup, value = 1)
        self.radioButtonUnderlined = ttk.Radiobutton(self, text = "Underlined", variable = buttonGroup, value = 2)
        
        #line 3
        self.productImage = tk.Image()


        self.itemNameAndPrice.pack(side = 'top')
        self.spinBox.pack(side = 'right')
        self.radioButtonBold.pack(side = 'left')
        self.radioButtonItalic.pack(side = 'top')
        self.radioButtonUnderlined.pack(side = 'right')
        self.productImage.pack(top)