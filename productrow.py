import tkinter as tk
from tkinter import ttk
import productframe

class ProductRow(tk.Frame):
    def __init__(self, parent = None, fontNames = {"Default 1", "Default 2", "Default 3"}):
        super().__init__(parent)
        self.parent=parent
        self.fontNames = fontNames
        
    def create_widgets(self):
        self.leftProduct = productframe.ProductFrame(self, "Left Item")
        self.centerProduct = productframe.ProductFrame(self, "center Item")
        self.rightProduct = productframe.ProductFrame(self, "right Item")