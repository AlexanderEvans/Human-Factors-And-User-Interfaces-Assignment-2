import tkinter as tk
from tkinter import ttk

class Payment(tk.Toplevel):
    def __init__(self, parent = None, reciept = "", total = 0, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.credentialFrame = tk.Frame(self)
        self.credentialFrame.First = tk.Entry(credentialFrame)
        self.credentialFrame.Last = tk.Entry(credentialFrame)
        self.credentialFrame.adress = tk.Entry(credentialFrame)
        self.credentialFrame.ccn = tk.Entry(credentialFrame)
        self.credentialFrame.ccv = tk.Entry(credentialFrame)
        self.credentialFrame.LFirst = tk.Label(credentialFrame, text = "First Name: ")
        self.credentialFrame.LLast = tk.Label(credentialFrame, text = "Last Name: ")
        self.credentialFrame.Ladress = tk.Label(credentialFrame, text = "Adress: ")
        self.credentialFrame.Lccn = tk.Label(credentialFrame, text = "Credit Card Number: ")
        self.credentialFrame.LccV = tk.Label(credentialFrame, text = "CCV: ")

