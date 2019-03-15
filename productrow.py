import tkinter as tk
from tkinter import ttk
import productframe

class ProductRow(tk.Frame):
    def __init__(self, parent = None, fontNames = {"Default 1", "Default 2", "Default 3"}, fontPrices = {1.99,2.99,3.99}):
        super().__init__(parent)
        self.parent=parent
        self.fontNames = fontNames
        self.fontPrices = fontPrices
        
    def create_widgets(self):
        self.leftProduct = productframe.ProductFrame(self, self.fontNames[1], self.fontPrices[1])
        self.centerProduct = productframe.ProductFrame(self, self.fontNames[2], self.fontPrices[2])
        self.rightProduct = productframe.ProductFrame(self, self.fontNames[3], self.fontPrices[3])
        self.leftProduct.pack(side = 'left')
        self.centerProduct.pack(side = 'left')
        self.rightProduct.pack(side = 'left')