from tkinter import *
from tkinter import messagebox

main = Tk()


def Submit():
    messagebox.askquestion("Form","Do you want to Submit")


# setting geometry of window
# instance
main.geometry("100x100")

# creating Window
B1 = Button(main, text="Submit", command=Submit)

# Button positioning
B1.pack()

# infinite loop till close
main.mainloop()
