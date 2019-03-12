
class ProductFrame(tk.Frame):
    def __init__(self, myStringVarList = [], parent = None):
        super().__init__(parent)
        self.parent=parent
        self.pack()
        self.create_widgets()
        self.myStringVarList = myStringVarList

    def create_widgets(self):
        #line one of frame:
        self.checkbox = ttk.Checkbutton(self)
        self.itemNameAndPrice = ttk.Label(self)
        self.spinBox = ttk.Spinbox(self)

        #line 2
        self.buttonGroup = StringVar()
        self.buttonGroup.set(0)
        self.radioButtonOne = ttk.Radiobutton(self, text = myStringVarList[1], variable = buttonGroup, value = 0)#I think array starts at 1 in python???
        self.radioButtonTwo = ttk.Radiobutton(self, text = myStringVarList[2], variable = buttonGroup, value = 1)
        self.radioButtonThree = ttk.Radiobutton(self, text = myStringVarList[3], variable = buttonGroup, value = 2)
        
        #line 3
        self.productImage = tk.Image()


        self.checkbox.pack(side = 'left')
        self.itemNameAndPrice.pack(side = 'top')
        self.spinBox.pack(side = 'right')
        self.radioButtonOne.pack(side = 'left')
        self.radioButtonTwo.pack(side = 'top')
        self.radioButtonThree.pack(side = 'right')
        self.productImage.pack(top)
