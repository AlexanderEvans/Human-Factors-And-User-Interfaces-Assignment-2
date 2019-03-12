import tkinter as tk
from tkinter import ttk
import productframe

class ProductRow(tk.Frame):
    def __init__(self, parent = None, text = "Default Text"):
        super().__init__(parent)
        self.parent=parent