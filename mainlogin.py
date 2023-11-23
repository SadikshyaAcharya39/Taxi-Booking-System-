                              # IMPORTING REQUIRED MODULES#
import pathlib
from tkinter import *
import sqlite3
from tkinter import messagebox

from customerlogin import customerloginClass
from adminlogin import adminloginClass
from driverlogin import driverloginClass

import PIL
from PIL import ImageTk, Image  # pip install pillow
#
new_path = pathlib.Path('.')/'t1.jpg'
# print(new_path)


                                    # MAIN LOGIN PAGE  #
class mainloginClass:
    def __init__(self):
        self.root = Tk()
        self.root.title("Sadikshya Acharya|| TAXI BOOKING SYSTEM")
        self.root.geometry('1350x718')
        self.root.state('zoomed')
        self.root.resizable(False, False)

      # Image
        image = PIL.Image.open('t1.jpg').resize((int(self.root.winfo_screenwidth()),
                                                 int(self.root.winfo_screenheight())))
        self.bg = ImageTk.PhotoImage(image)
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0)


        # frame
        frame_register = Frame(self.root, bg="white")
        frame_register.place(x=850, y=300, height=250, width=300)
        # title
        title = Label(frame_register, text=" Gain Access To? ", font=("Times New Roman", 20),fg='orange', bg='white')
        title.place(x=80, y=15)
        line = Label(frame_register, text='___________________________________________', fg='black', bg='white')
        line.place(x=50, y=45)

        button = Button(frame_register, text="Customer", command=self.cuslog, font=("Times New Roman", 18),fg='orange', bg='white').place(x=80, y=90, height=30, width=150)
        button = Button(frame_register, text="Driver", command=self.drlog, font=("Times New Roman", 18),fg='orange', bg='white').place(x=80, y=140, height=30, width=150)
        button = Button(frame_register, text="Administrator", command=self.adlog, font=("Times New Roman", 18),
                        fg='orange', bg='white').place(x=80, y=190, height=30, width=150)

        # Title(Heading)
        self.txt = 'Here To There'
        self.heading = Label(self.root, text=self.txt, font=('Times New Roman', 30, 'bold'), bg='orange',
                             fg='white')
        self.heading.place(x=0, y=0, width=1500, height=40)

    def cuslog(self):
        self.root.destroy()
        self.new_obj = customerloginClass()

    def adlog(self):
        self.root.destroy()
        self.new_obj = adminloginClass()

    def drlog(self):
        self.root.destroy()
        self.new_obj = driverloginClass()

#
# if __name__ == "__main__":
#     obj = mainloginClass()
#     mainloop()


