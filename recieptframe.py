import tkinter as tk
from tkinter import ttk

class RecieptFrame(tk.Frame):
    def __init__(self, parent = None, reciept = "", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.items = tk.Label(self, text = "Items:")
        self.litems = tk.Label(self, text = reciept)
        
        self.items.grid(row = 0, column = 0)
        self.litems.grid(row = 1, column = 0)
