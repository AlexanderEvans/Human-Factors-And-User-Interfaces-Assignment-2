import tkinter as tk
from tkinter import ttk
import credentialframe
import recieptframe


class TotalFrame(tk.Frame):
    def __init__(self, parent = None, total = 0, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.costTotal = tk.Label(self, text = "Subtotal")
        self.cost = repr(total)
        self.lcost = tk.Label(self, text = self.cost)
        
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
        
class Payment(tk.Toplevel):
    def __init__(self, parent = None, reciept = "", total = 0, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.credentialFrame = credentialframe.CredentialFrame(self)
        self.items = recieptframe.RecieptFrame(self, reciept)
        self.totals = TotalFrame(self, total)
        self.btn = tk.Button(self, command = self.quit, text = "Place Order")

        self.credentialFrame.grid(row = 0, column = 0, columnspan = 2)
        self.items.grid(row = 1, column = 0)
        self.totals.grid(row = 1, column = 2)
        self.btn.grid(row = 2, column = 0, columnspan = 2)


