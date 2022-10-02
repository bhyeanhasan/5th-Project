from tkinter import RIDGE, filedialog
from tkinter import *
from tkinter import ttk


class FrontEnd:
    def __init__(self, master):
        self.master = master

        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()

        #         ttk.Label(self.frame_header, image=self)
        ttk.Label(self.frame_header, text='PhotoHub').grid(
            row=0, column=2, columnspan=1)
        ttk.Label(self.frame_header, text='An Image Editor Just For You!').grid(
            row=1, column=1, columnspan=3)

        self.frame_menu = ttk.Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(relief=RIDGE, padding=(50, 15))

        ttk.Button(
            self.frame_menu, text="Upload An Image", command=self.upload_action).grid(
            row=0, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Crop Image", command=self.crop_action).grid(
            row=1, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Add Text", command=self.text_action_1).grid(
            row=2, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Draw Over Image", command=self.draw_action).grid(
            row=3, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Apply Filters", command=self.filter_action).grid(
            row=4, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Blur/Smoothening", command=self.blur_action).grid(
            row=5, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Adjust Levels", command=self.adjust_action).grid(
            row=6, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Rotate", command=self.rotate_action).grid(
            row=7, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Flip", command=self.flip_action).grid(
            row=8, column=0, columnspan=2, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Save As", command=self.save_action).grid(
            row=9, column=0, columnspan=2, padx=5, pady=5, sticky='sw')
    def upload_action(self):
        self.canvas.delete("all")
        self.filename = filedialog.askopenfilename()
        self.original_image = cv2.imread(self.filename)

        self.edited_image = cv2.imread(self.filename)
        self.filtered_image = cv2.imread(self.filename)
        self.display_image(self.edited_image)

    def text_action_1(self):
        pass

    def crop_action(self):
        pass

    def start_crop(self, event):
        pass

    def crop(self, event):
        pass

    def end_crop(self, event):
        pass

    def text_action(self):
        pass

    def end_text_crop(self, event):
        pass


    def draw_action(self):
        pass

    def choose_color(self):
        pass


    def start_draw(self, event):
        pass


    def draw(self, event):
        pass


    def refresh_side_frame(self):
        pass


    def filter_action(self):
        pass


    def blur_action(self):
        pass


    def rotate_action(self):
        pass


    def flip_action(self):
        pass


    def adjust_action(self):
        pass


    def save_action(self):
        pass


    def negative_action(self):
        pass


    def bw_action(self):
        pass


    def stylisation_action(self):
        pass


    def sketch_action(self):
        pass


    def emb_action(self):
        pass


    def sepia_action(self):
        pass


    def binary_threshold_action(self):
        pass


    def erosion_action(self):
        pass


    def dilation_action(self):
        pass


    def averaging_action(self, value):
        pass


    def gaussian_action(self, value):
        pass


    def median_action(self, value):
        pass


    def brightness_action(self, value):
        pass


    def saturation_action(self, event):
        pass


    def rotate_left_action(self):
        pass


    def rotate_right_action(self):
        pass


    def vertical_action(self):
        pass


    def horizontal_action(self):
        pass


    def apply_action(self):
        pass


    def cancel_action(self):
        pass


    def revert_action(self):
        pass


    def display_image(self, image=None):
        pass

mainWindow = Tk()
FrontEnd(mainWindow)
mainWindow.mainloop()
