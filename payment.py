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

class Payment(tk.Toplevel):
    def __init__(self, parent = None, reciept = "", total = 0, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.credentialFrame = CredentialFrame(self)
        self.credentialFrame.pack()


