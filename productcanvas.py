import tkinter as tk
from tkinter import ttk
import productrow
#hardcoded for now, make a row of 3 pruducts.

def makeProducts(parent):
    #make product rows
    r1 = productrow.ProductRow(parent = parent, fn1 = 'L1: ', fn2 = 'C1: ', fn3 = 'R1: ', fp1 = 1.49, fp2 =  2.49, fp3 =  3.49)
    r2 = productrow.ProductRow(parent = parent, fn1 = 'L2: ', fn2 = 'C2: ', fn3 = 'R2: ', fp1 = 4.49, fp2 =  5.49, fp3 =  6.49)
    r3 = productrow.ProductRow(parent = parent, fn1 = 'L3: ', fn2 = 'C3: ', fn3 = 'R3: ', fp1 = 7.49, fp2 =  8.49, fp3 =  9.49)

    #r1.grid(row = 0, column = 0, sticky = 'new', padx = 10, pady = 10)
    #r2.grid(row = 1, column = 0, sticky = 'new', padx = 10, pady = 10)
    #r3.grid(row = 2, column = 0, sticky = 'new', padx = 10, pady = 10)

    r1.pack(side = 'top')
    r2.pack(side = 'top')
    r3.pack(side = 'top')
    array = {r1, r2, r3}
    return array

class ProductCanvas(tk.Canvas):
    def __init__(self, parent = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.frame = tk.Frame(self);
        self.window = self.create_window((0,0),window=self.frame,anchor='nw')
        self.frame.pack(expand = 1)
        makeProducts(self.frame)
        