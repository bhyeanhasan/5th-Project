import cv2
from tkinter import Tk, ttk

def hide(which):
    which.pack_forget()

page = Tk()
page.title("NoYoN")
page.geometry('550x450+350+150')

top_part = ttk.Frame(page)
top_part.pack()
ttk.Label(top_part, text="New").grid(row=0, column=0)
ttk.Label(top_part, text="bhyean").grid(row=0, column=1)

side_part = ttk.Frame(page)
side_part.pack()





ttk.Button(side_part, text='Hide', compound=hide(side_part)).grid(row=0, column=0)

page.mainloop()
