############# IMPORTING ALL THE NECESSARY MODULES  ############
import pathlib
from sqlite3.dbapi2 import Cursor, Row
from tkinter import *
import sqlite3

import PIL
from PIL import Image, ImageTk
from tkinter import messagebox
from driverpage import driverpageClass
######## FOR CONNECTION ##########
import mysql.connector
new_path = pathlib.Path('.')/'t1.jpg'
# print(new_path)

############### CREATING CLASS ###########
############ DRIVER LOGIN PAGE #########
class driverloginClass():
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

        # frame
        frame_driverlogin = Frame(self.root, bg="white")
        frame_driverlogin.place(x=400, y=150, height=250, width=550)

        title = Label(frame_driverlogin, text=" WELCOMEEE ", font=("Times New Roman", 20), fg='orange', bg='white')
        title.place(x=160, y=15)

        self.Email = StringVar()
        self.Password = StringVar()

        # username label and entry
        dri_user_name = Label(frame_driverlogin, text="Email", font=("Times New Roman", 18), bg="white")
        dri_user_name.place(x=20, y=80, height=30, width=110)
        dri_user_entry = Entry(frame_driverlogin, textvariable=self.Email, font=("Times New Roman", 14))
        dri_user_entry.place(x=170, y=80, height=30, width=240)

        ####### password label and entry
        dri_password = Label(frame_driverlogin, text="Password", font=("Times New Roman", 18), bg="white")
        dri_password.place(x=35, y=130, height=30, width=110)
        dri_pass_entry = Entry(frame_driverlogin, show="*", textvariable=self.Password, font=("times new roman", 14))
        dri_pass_entry.place(x=170, y=130, height=30, width=240)

        ##### forget password button
        drilog_Button = Button(frame_driverlogin, text=" Forget Password? ", font=("Times New Roman", 18),bg="orange", fg="white").place(x=40,
                                                                                                                 y=180,
                                                                                                                 height=35)

        # button for login
        drilog_Button = Button(frame_driverlogin, text=" Login ", command=self.drivFunc, font=("Times New Roman", 18),bg="orange", fg="white"
                               )
        drilog_Button.place(x=300, y=180,height=35)

        ######button for exit
        drilog_Button = Button(frame_driverlogin, text="Exit ", command=exit, font=("Times New Roman", 18),bg="orange", fg="white",
                              )
        drilog_Button.place(x=425, y=180,height=35)

        # Title(Heading)
        self.txt = 'Here To There'
        self.heading = Label(self.root, text=self.txt, font=('Times New Roman', 30, 'bold'), bg='orange',
                             fg='white')
        self.heading.place(x=0, y=0, width=1500, height=40)

        ###################   database connection    ####################

    def drivFunc(self):
        email = self.Email.get()
        con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
        cur = con.cursor()
        con.commit()
        if self.Email == "" or self.Password == "":
            messagebox.showerror("error", "all the fields are required", parent=self.root)
        else:
            try:
                cur.execute('SELECT * FROM taxi_driver WHERE email=%s and passwords=%s',
                            (email, self.Password.get()))
                row = cur.fetchone()

                # if row == None:
                #     messagebox.showerror("error", 'INVALID email and password', parent=self.root)

                messagebox.showinfo("success", 'welcome, have a safe drive', parent=self.root)
                self.dasboard(email)
                con.close()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


    def dasboard(self, email):
        self.root.destroy()
        import driverpage
        obj = driverpage.driverpageClass(self.root, email)



if __name__ == "__main__":
    obj = driverloginClass()
    mainloop()