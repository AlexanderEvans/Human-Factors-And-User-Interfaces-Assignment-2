import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def invalidInputWarning():
    rtnVal = False
    if messagebox.askyesno(title = 'Invalid Input Warning!', message = 'Warning!  You are attempting to purchase "0" of at least one product!  Do you want to remove these items from your cart and proceed anyway?'):
        rtnVal = True
    return rtnVal

def displayConfirmationPopup():
    messagebox.showinfo(title = 'Order success! ', message = 'Congratulations!  Your order has been placed successfully!')
    
def invalidPaymentCredentialsError():
    messagebox.showerror(title = 'Error! ', message = 'Error: Invalid payment credentials were detected.  Please try again.')


