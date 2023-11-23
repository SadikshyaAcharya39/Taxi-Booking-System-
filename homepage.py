#########IMPORTING REQUIRED MODULES
import pathlib
from tkinter import *
import sqlite3
from tkinter import messagebox

import PIL

from register import registerClass
from mainlogin import mainloginClass

import PIL
from PIL import ImageTk, Image  # pip install pillow
#
new_path = pathlib.Path('.')/'t1.jpg'
# print(new_path)

############CLASS(OBJECT ORIENTED)#######################
##########    MAKING OF HOMEPAGE  ###################
class homepageClass:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1350x718')
        self.root.title("Sadikshya Acharya|| TAXI BOOKING SYSTEM")
        self.root.state('zoomed')
        self.root.resizable(False, False)


          # Image
        image = PIL.Image.open('t1.jpg').resize((int(self.root.winfo_screenwidth()),
                                                 int(self.root.winfo_screenheight())))
        self.bg = ImageTk.PhotoImage(image)
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0)

        # Title(Heading)
        self.txt = 'Here To There'
        self.heading = Label(self.root, text=self.txt, font=('Times New Roman', 30, 'bold'), bg='orange',
                             fg='white')
        self.heading.place(x=0, y=0, width=1500, height=40)

        # # label
        # label = Label(self.root, text="Here To Theree", font=("Times New Roman", 18), bg= "orange", foreground="white")
        # label.place(x=500, y=0)

        # buttons
        myButton = Button(self.root, text="Sign In ", command=self.Log, font=("Times New Roman", 15), padx=30, pady=10,
                          bg="orange")
        myButton.place(x=850, y=520)
        myButton = Button(self.root, text="Sign Up", command=self.Reg, font=("Times New Roman", 15), padx=30, pady=10,
                          bg="orange")
        myButton.place(x=1100, y=520)

    ############## FUNCTION TO CONNECT REGISTER BUTTON WITH REGISTERCLASS ################
    def Reg(self):
        self.root.destroy()
        self.new_obj = registerClass()

    ############## FUNCTION TO CONNECT LOGIN BUTTON WITH MAINLOGINCLASS ###########
    def Log(self):
        self.root.destroy()
        self.new_obj = mainloginClass()
#

if __name__ == "__main__":
    obj = homepageClass()
    mainloop()


