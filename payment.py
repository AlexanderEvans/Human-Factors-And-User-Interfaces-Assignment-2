import tkinter as tk
from tkinter import ttk
import credentialframe
import recieptframe
import totalframe


        
class Payment(tk.Toplevel):
    def __init__(self, parent = None, reciept = "", total = 0, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.credentialFrame = credentialframe.CredentialFrame(self)
        self.items = recieptframe.RecieptFrame(self, reciept)
        self.totals = totalframe.TotalFrame(self, total)
        self.btn = tk.Button(self, command = self.quit, text = "Place Order")

        self.credentialFrame.grid(row = 0, column = 0, columnspan = 2)
        self.items.grid(row = 1, column = 0)
        self.totals.grid(row = 1, column = 2)
        self.btn.grid(row = 2, column = 0, columnspan = 2)


