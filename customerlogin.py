#############CUSTOMER LOGIN PAGE WIHT TKINGER ###############

#############IMPORTING ALL THE REQUIRED MODULES
import pathlib
from logging import exception
from tkinter import *
###########FOR IMPORTING IMAGE
from PIL import Image, ImageTk
##########FOR IMPORTING MESSAGE BOX
from tkinter import messagebox
##########FOR ttk COMBOBOX
from tkinter import ttk
#########FOR IMPORTING AND CONNECTING WITH BOOKINGCLASS PAGE
from booking1 import bookingClass
##########FOR CONNECTING WITH MYSQL WORKBENCH
import mysql.connector


import PIL
from PIL import ImageTk, Image  # pip install pillow
#
new_path = pathlib.Path('.')/'t1.jpg'
# print(new_path)

##########CREATING CLASS CUSTOMERLOGINCLASS AND CUSTOMER LOIGN PAGE
class customerloginClass():



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


        ##############FRAME IN THE PAGE FOR LOGIN
        frame_customerlogin = Frame(self.root, bg="white")
        frame_customerlogin.place(x=400, y=150, height=250, width=450)

        title = Label(frame_customerlogin, text=" CusLogin Form ", font=("Times New Roman", 20), fg='orange', bg='white')
        title.place(x=140, y=15)

         ############VARIABLE DECLARATION
        self.Email = StringVar()
        self.Password = StringVar()
        self.securityanswer = StringVar()
        self.newpassword = StringVar()

        ################  USERNAME
        cus_user_name = Label(frame_customerlogin, text="Email", font=("Times New Roman", 18), bg="white")
        cus_user_name.place(x=20, y=80, height=30, width=110)
        cus_user_entry = Entry(frame_customerlogin, textvariable=self.Email, font=("Times New Roman", 16))
        cus_user_entry.place(x=170, y=80, height=30, width=240)

        #############  PASSWORD
        cus_password = Label(frame_customerlogin, text="Password", font=("Times New Roman", 18), bg="white")
        cus_password.place(x=35, y=130, height=30, width=110)
        cus_pass_entry = Entry(frame_customerlogin, show="*", textvariable=self.Password, font=("Times New Roman", 16))
        cus_pass_entry.place(x=170, y=130, height=30, width=240)

        ##############FORGET PASSWORD
        cuslog_Button = Button(frame_customerlogin, command=self.forget, text=" Forget Password? ",
                               font=("Times New Roman", 18),bg="orange", fg="white").place(x=40, y=190, height=35)

        ############# BUTTON FOR LOGIN
        cuslog_Button = Button(frame_customerlogin, text=" Login ", command=self.cusloginFunc,
                               font=("Times New Roman", 18),bg="orange", fg="white")
        cuslog_Button.place(x=250, y=190,height=35)

        ############ BUTTON FOR EXIT
        cuslog_Button = Button(frame_customerlogin, text="Exit ", command=exit, font=("Times New Roman", 18),bg="orange", fg="white"
                               )
        cuslog_Button.place(x=350,y=190,height=35)

        ############ DATABASE FOR CONNECTION WITH MYSQL WITH VALIDATION

    def cusloginFunc(self):
        email = self.Email.get()

        con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
        cur = con.cursor()
        con.commit()
        if self.Email == "" or self.Password == "":
            messagebox.showerror("Message", "All the fields are required to fill", parent=self.root)

        else:
            try:
                cur.execute('SELECT * FROM register WHERE cemail=%s and Passwords=%s',
                            (email, self.Password.get()))
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror("Message", 'All fields are required to fill', parent=self.root)
                else:
                    messagebox.showinfo("Success", 'WELCOME CUSTOMER!!', parent=self.root)
                    self.book(email)
                    # self.root.destroy()
                    # self.new_obj = bookingClass(email)
                    # from booking1 import globalIni
                    # globalIni(row[5])
                con.close()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def book(self,email):
       self.root.destroy()
       import booking1
       obj=booking1.bookingClass(self.root,email)

    #################### RESET PASSWORD #######################
    def resetpassword(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
        cur = con.cursor()
        con.commit()
        if self.cmb_quest == "Select" or self.securityanswer == "" or self.newpassword == "":
            messagebox.showerror("Error", "All the fields are required to reset the new password", parent=self.root)
        else:
            try:
                cur.execute("SELECT * FROM register WHERE cemail=%s and question=%s and security_answer=%s",
                            (self.Email.get(), self.cmb_quest.get(), self.securityanswer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Enter valid security question and answer", parent=self.root)
                else:
                    cur.execute("UPDATE register SET passwords=%s where cemail=%s",
                                (self.newpassword.get(), self.Email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Password is reset successfully", parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

        ############## FOR FORGET PASSWORD PAGE

    def forget(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
        cur = con.cursor()
        con.commit()
        if self.Email.get() == "":
            messagebox.showerror("Error", "Please enter your email to reset your password", parent=self.root)
        else:
            try:
                cur.execute("SELECT * FROM register WHERE cemail=%s", (self.Email.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Enter valid email", parent=self.root)
                else:
                    self.root2 = Toplevel()
                    self.root2.title("forget password")
                    self.root2.geometry("400x350+490+100")
                    self.root2.config(bg="grey")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    t = Label(self.root2, text="Forgot Password?", font=("times new roman", 20, "bold"), fg="white",
                              bg="orange").place(x=100, y=0)

                    ############SECURITY QUESTION
                    question = Label(self.root2, text="Security Question", font=("Times New Roman", 18)).place(x=10,
                                                                                                               y=60,
                                                                                                               height=30)
                    self.cmb_quest = ttk.Combobox(self.root2, font=("Times new Roman", 18))
                    self.cmb_quest['values'] = (
                    "Select","Your favourite Pet Name", "Your Birthplace", "", "Your Best Friend Name")
                    self.cmb_quest.place(x=10, y=100, height=30)
                    self.cmb_quest.current(0)
                    ##########ANSWER
                    answer = Label(self.root2, text="Answer", font=("Times New Roman", 18)).place(x=10, y=140,
                                                                                                  height=30)
                    entry = Entry(self.root2, font=("Times New Roman", 18), textvariable=self.securityanswer,
                                  bg="white").place(x=170, y=140, height=30, width=210)
                    ##########NEW PASSWORD
                    label = Label(self.root2, text="New password", font=("Times New Roman", 15), bg="white").place(x=10,
                                                                                                                   y=200)
                    entry = Entry(self.root2, textvariable=self.newpassword, font=("Times New Roman", 15),
                                  bg="light grey").place(x=170, y=190, height=30, width=210)
                    ############ PASSWORD SETUP BUTTON
                    change_Button = Button(self.root2, text="Reset password ", command=self.resetpassword,
                                           font=("Times New Roman", 18),
                                           bg="light blue").place(x=100, y=240)

                con.close()

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

#
# if __name__ == "__main__":
#     obj = customerloginClass()
#     mainloop()