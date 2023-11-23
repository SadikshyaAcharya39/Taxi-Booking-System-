                                                #IMPORTING REQUIRED MODULES #
import pathlib
from tkinter import *

import PIL
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from adminpage1 import adminpageClass

import PIL
from PIL import ImageTk, Image  # pip install pillow
#
new_path = pathlib.Path('.')/'t1.jpg'
# print(new_path)


                                                          #CREATING CLASS #
                                                # CREATING ADMIN LOGIN PAGE #
class adminloginClass():
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

                                                    # frame

        frame_adminlogin = Frame(self.root, bg="white")
        frame_adminlogin.place(x=400, y=150, height=250, width=550)

        title = Label(frame_adminlogin, text=" WELCOMEEE ", font=("Times New Roman", 20), fg='orange', bg='white')
        title.place(x=160, y=15)



                                                 #VARIABLE DECLARATION
        self.Email = StringVar()
        self.Password = StringVar()

                                               # username and password label and entry
        ad_email = Label(frame_adminlogin, text="Email", font=("Times New Roman", 18), bg="white")
        ad_email.place(x=20, y=80, height=30, width=110)
        ad_email_entry = Entry(frame_adminlogin, textvariable=self.Email, font=("Times New Roman", 14))
        ad_email_entry.place(x=170, y=80, height=30, width=240)



        cus_password = Label(frame_adminlogin, text="Password", font=("Times New Roman", 18), bg="white")
        cus_password.place(x=35, y=130, height=30, width=110)
        cus_pass_entry = Entry(frame_adminlogin, show="*", textvariable=self.Password, font=("Times new Roman", 14))
        cus_pass_entry.place(x=170, y=130, height=30, width=240)


        cuslog_Button = Button(frame_adminlogin, text=" Forget Password? ", font=("Times New Roman", 18),bg="orange",
                               fg="white" ).place(x=40,
                                                                                                                y=180,
                                                                                                                height=35)

        # button
        cuslog_Button = Button(frame_adminlogin, text=" Login ", command=self.adminloginFunc,
                               font=("Times New Roman", 18), bg="orange", fg="white")

        cuslog_Button.place(x=300, y=180, height=35)

        cuslog_Button = Button(frame_adminlogin, text="Exit ", command=exit, font=("Times New Roman", 18),bg="orange",
                               fg="white" )
        cuslog_Button.place(x=425, y=180, height=35)


    # database
    def adminloginFunc(self):

        # database

        con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
        cur = con.cursor()
        con.commit()
        if self.Email == "" or self.Password == "":
            messagebox.showerror("Error", "All the fields are required to fill", parent=self.root)
        else:
            try:
                cur.execute('SELECT * FROM Co_staff WHERE staff_email = %s and passwords = %s',
                            (self.Email.get(), self.Password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", 'Invalid Email and Password', parent=self.root)
                else:
                    messagebox.showinfo("Success", 'WELCOMEE "ADMIN"', parent=self.root)
                    self.root.destroy()
                    self.new_object = adminpageClass()
                con.close()

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

#
# if __name__ == "__main__":
#     obj = adminloginClass()
#     mainloop()