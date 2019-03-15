import tkinter as tk
from tkinter import ttk

class TotalFrame(tk.Frame):
    def __init__(self, parent = None, total = 0, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.costTotal = tk.Label(self, text = "Subtotal")
        self.cost = repr(total)
        self.lcost = tk.Label(self, text = self.cost)

        self.DiscountTotal = tk.Label(self, text = "Discount")
        
        self.dis = "Discounted"
        if total<10.00:
            self.dis = "No discount!"
        self.ldis = tk.Label(self, text = self.cost)
        
        self.costTotal.grid(row = 0, column = 0)
        self.lcost.grid(row = 0, column = 1)

        self.tax = tk.Label(self, text = "Tax at 15%: ")
        self.taxNum = repr(float(total)*0.15)
        self.ltax = tk.Label(self, text = self.taxNum)
        
        self.tax.grid(row = 1, column = 0)
        self.ltax.grid(row = 1, column = 1)

        self.taxTot = tk.Label(self, text = "Total: ")
        self.taxTotNum = repr(float(total)*1.15)
        self.ltaxTot = tk.Label(self, text = self.taxTotNum)
        
        self.taxTot.grid(row = 2, column = 0)
        self.ltaxTot.grid(row = 2, column = 1)
        self.DiscountTotal.grid(row = 3, column = 0)
        self.ldis.grid(row = 3, column = 1)
