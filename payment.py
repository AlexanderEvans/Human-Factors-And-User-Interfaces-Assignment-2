import tkinter as tk
from tkinter import ttk

class CredentialFrame(tk.Frame):
    def __init__(self, parent = None, reciept = "", total = 0, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.First = tk.Entry(self)
        self.Last = tk.Entry(self)
        self.adress = tk.Entry(self)
        self.ccn = tk.Entry(self)
        self.ccv = tk.Entry(self)
        self.LFirst = tk.Label(self, text = "First Name: ")
        self.LLast = tk.Label(self, text = "Last Name: ")
        self.Ladress = tk.Label(self, text = "Adress: ")
        self.Lccn = tk.Label(self, text = "Credit Card Number: ")
        self.Lccv = tk.Label(self, text = "CCV: ")
        
        self.First.grid(row = 0, column = 1)
        self.LFirst.grid(row = 0, column = 0)

        self.Last.grid(row = 2, column  = 1)
        self.LLast.grid(row = 2, column = 0)

        self.adress.grid(row = 3, column = 1)
        self.Ladress.grid(row = 3, column = 0)

        self.ccn.grid(row = 4, column = 1)
        self.Lccn.grid(row = 4, column = 0)

        self.ccv.grid(row = 5, column = 1)
        self.Lccv.grid(row = 5, column = 0)

class RecieptFrame(tk.Frame):
    def __init__(self, parent = None, reciept = "", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.items = tk.Label(self, text = "Items:")
        self.litems = tk.Label(self, text = reciept)
        
        self.items.grid(row = 0, column = 0)
        self.litems.grid(row = 1, column = 0)

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
        self.credentialFrame = CredentialFrame(self)
        self.credentialFrame.grid(row = 0, column = 0, columnspan = 2)
        self.items = RecieptFrame(self, reciept)
        self.totals = TotalFrame(self, total)
        self.items.grid(row = 1, column = 0)
        self.totals.grid(row = 1, column = 2)
        self.btn = tk.Button(self, command = self.quit, text = "Place Order")
        self.btn.grid(row = 2, column = 0, columnspan = 2)

