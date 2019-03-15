import tkinter as tk
from tkinter import ttk
import productframe

class ProductRow(tk.Frame):
    def __init__(self, parent = None, fn1 = "Default 1", fn2 = "Default 2", fn3 =  "Default 3", fp1 = 1.99, fp2 = 2.99, fp3 = 3.99):
        super().__init__(parent)
        self.parent=parent
        self.leftProduct = productframe.ProductFrame(self, fn1, fp1)
        self.centerProduct = productframe.ProductFrame(self, fn2, fp2)
        self.rightProduct = productframe.ProductFrame(self, fn3, fp3)
        self.leftProduct.pack(side = 'left', expand = 1)
        self.centerProduct.pack(side = 'left', expand = 1)
        self.rightProduct.pack(side = 'left', expand = 1)
        