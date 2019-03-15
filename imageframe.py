import tkinter as tk
from tkinter import ttk

class ImageFrame(tk.Canvas):
    def __init__(self, parent, imageName = "default", imageExt = ".GIF", *args, **kwargs):
        self.photoPath = "./"+imageName+imageExt
        self.photo = tk.PhotoImage(file = self.photoPath)
        super().__init__(parent, width = self.photo.width(), height = self.photo.height(), *args, **kwargs)
        self.create_image(0, 0, image=self.photo, anchor="nw")
