import cv2
from PIL import ImageTk, Image
from tkinter import (ttk, Tk, Canvas, filedialog, messagebox)


class Design:
    def __init__(self, master):
        self.master = master
        self.menu_initialisation()

    def menu_initialisation(self):
        self.master.geometry('550x450+250+10')
        self.master.title('Md. Babul Hasan 1802027')

        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()
        ttk.Label(self.frame_header, text='Image Editor').grid(row=0, column=2, columnspan=1)
        ttk.Label(self.frame_header, text='5th Semester Project').grid(row=1, column=1, columnspan=3)

        self.frame_menu = ttk.Frame(self.master)
        self.frame_menu.pack()
        ttk.Button(
            self.frame_menu, text="Upload An Image", command=self.upload_action).grid(
            row=0, column=0, columnspan=2, padx=5, pady=5, sticky='sw')
        ttk.Button(
            self.frame_menu, text="Save As", command=self.save_action).grid(
            row=1, column=0, columnspan=2, padx=5, pady=5, sticky='sw')
        self.canvas = Canvas(self.frame_menu, bg="gray", width=300, height=400)
        self.canvas.grid(row=0, column=3, rowspan=10)

    def upload_action(self):
        self.canvas.delete("all")
        self.filename = filedialog.askopenfilename()
        self.original_image = cv2.imread(self.filename)
        self.edited_image = cv2.imread(self.filename)
        self.filtered_image = cv2.imread(self.filename)
        self.display_image(self.edited_image)

    def save_action(self):
        original_file_type = self.filename.split('.')[-1]
        filename = filedialog.asksaveasfilename()
        filename = filename + "." + original_file_type
        save_as_image = self.edited_image
        cv2.imwrite(filename, save_as_image)
        self.filename = filename
        messagebox.showinfo(title="Done", message="Image Saved")

    def display_image(self, image=None):
        self.canvas.delete("all")
        if image is None:
            image = self.edited_image.copy()
        else:
            image = image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.new_image = cv2.resize(image, (300, 400))
        self.new_image = ImageTk.PhotoImage(Image.fromarray(self.new_image))
        self.canvas.config(width=300, height=400)
        self.canvas.create_image(300 / 2, 400 / 2, image=self.new_image)


Page = Tk()
Design(Page)
Page.mainloop()
