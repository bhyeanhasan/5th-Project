from tkinter import (ttk, Tk, PhotoImage, Canvas, filedialog, colorchooser, RIDGE,
                     GROOVE, ROUND, Scale, HORIZONTAL)
import cv2
from PIL import ImageTk, Image
import numpy as np


class Design:
    def __init__(self, master):
        self.master = master

        # Header frame:
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()
        ttk.Label(self.frame_header, text='Image Editor').grid(row=0, column=2, columnspan=1)
        ttk.Label(self.frame_header, text='5th semester project').grid(row=1, column=1, columnspan=3)

        # Menu Frame
        self.frame_menu = ttk.Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(relief=RIDGE, padding=(15, 15))
        ttk.Button(self.frame_menu, text="Upload An Image", command=self.upload_action).grid(row=0, column=0,columnspan=2, padx=5,pady=5, sticky='sw')
        ttk.Button(self.frame_menu, text="Save As", command=self.display_image).grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        self.canvas = Canvas(self.frame_menu, bg="white", width=300, height=400)
        self.canvas.grid(row=0, column=3, rowspan=10)



    def upload_action(self):
        self.canvas.delete("all")
        self.filename = filedialog.askopenfilename()
        self.original_image = cv2.imread(self.filename)
        self.edited_image = cv2.imread(self.filename)
        self.filtered_image = cv2.imread(self.filename)
        self.display_image(self.edited_image)

    def display_image(self, image=None):
        self.canvas.delete("all")
        if image is None:
            image = self.edited_image.copy()
        else:
            image = image

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channels = image.shape
        ratio = height / width

        new_width = width
        new_height = height

        if height > 400 or width > 300:
            if ratio < 1:
                new_width = 300
                new_height = int(new_width * ratio)
            else:
                new_height = 400
                new_width = int(new_height * (width / height))

        self.ratio = height / new_height
        self.new_image = cv2.resize(image, (new_width, new_height))

        self.new_image = ImageTk.PhotoImage(Image.fromarray(self.new_image))

        self.canvas.config(width=new_width, height=new_height)
        self.canvas.create_image(new_width / 2, new_height / 2, image=self.new_image)


mainWindow = Tk()
Design(mainWindow)
mainWindow.mainloop()
