                                           #IMPORTING  REQUIRED MODULES#
# FOR TKINTER
import pathlib


from tkinter import *
# THIS IS FOR CONNECTING WITH SQLITE
import sqlite3


# REQUIRED FOR MESSAGE BOX
from tkinter import messagebox

                                           # CONNECTING TWO PAGES#

from mainlogin import mainloginClass
from tkinter import ttk

import PIL
from PIL import ImageTk, Image  # pip install pillow
new_path = pathlib.Path('.')/'t1.jpg'
# print(new_path)


                                          # CONNECTING WITH MYSQL#
import mysql.connector


                                          #CREATING  CLASS AND WINDOW #
class registerClass():
    def __init__(self):
        self.root = Tk()
        self.root.title("Sadikshya Acharya|| TAXI BOOKING SYSTEM")
        self.root.geometry('1350x718')
        self.root.state('zoomed')
        self.root.resizable(False, False)
        self.root.configure(background="orange")


                                        # Image #
        image = PIL.Image.open('t1.jpg').resize((int(self.root.winfo_screenwidth()),
                                                 int(self.root.winfo_screenheight())))
        self.bg = ImageTk.PhotoImage(image)
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0)

                                        #VARIABLE DECLARATION#
        self.Firstname = StringVar()
        self.Lastname = StringVar()
        self.Gender = StringVar()
        self.Address = StringVar()
        self.Phonenumber = IntVar()
        self.Email = StringVar()
        self.Creditcardno = IntVar()
        self.Username = StringVar()
        self.Password = StringVar()
        self.Confirmpassword = StringVar()
        self.question = StringVar()
        self.var_chk = IntVar()
        self.securityanswer = StringVar()
        self.cmb_quest = StringVar()

                                                       #FRAME#

        frame_register = Frame(self.root, bg="white")
        frame_register.place(x=760, y=10, height=630, width=500)

                                                  #TITLE#
        title = Label(frame_register, text="Registration Form", font=("Times New Roman", 20, "bold"),fg='orange', bg='white')
        title.place(x=180, y=9)
        line = Label(frame_register, text='____________________________________________', fg='black', bg='white')
        line.place(x=180, y=42)
                                                 # FIRSTNAME

        label = Label(frame_register, text="First name", font=("Times New Roman", 18), bg="white").place(x=20, y=70,
                                                                                                         )
        entry = Entry(frame_register, font=("Times New Roman", 18), textvariable=self.Firstname, bg="white").place(x=260,
                                                                                                                y=70,
                                                                                                               height=25, width=220)
                                                  #LAST NAME
        label = Label(frame_register, text="Last name", font=("Times New Roman", 18), bg="white").place(x=20, y=110,
                                                                                                        )
        entry = Entry(frame_register, font=("Times New Roman", 18), textvariable=self.Lastname, bg="white").place(x=260,
                                                                                                               y=110,
                                                                                                               height=25, width=220)
                                                  #GENDER
        label = Label(frame_register, text="Gender", font=("Times New Roman", 18), bg="white").place(x=20, y=150,
                                                                                                     )
        entry = Entry(frame_register, font=("Times New Roman", 18), textvariable=self.Gender, bg="white").place(x=260,
                                                                                                             y=150,
                                                                                                             height=25, width=220)
                                                 #ADDRESS
        label = Label(frame_register, text="Address", font=("Times New Roman", 18), bg="white").place(x=20, y=190,
                                                                                                      )
        entry = Entry(frame_register, font=("Times New Roman", 18), textvariable=self.Address, bg="white").place(x=260,
                                                                                                              y=190,
                                                                                                              height=25, width=220)
                                                   #PHONE
        label = Label(frame_register, text="Phone", font=("Times New Roman", 18), bg="white").place(x=20, y=230,
                                                                                                   )
        entry = Entry(frame_register, font=("Times New Roman", 18), textvariable=self.Phonenumber, bg="white").place(x=260,
                                                                                                                  y=230,
                                                                                                                  height=25, width=220)
                                                   #EMAIL
        label = Label(frame_register, text="Email", font=("Times New Roman", 18), bg="white").place(x=20, y=270,
                                                                                                    )
        entry = Entry(frame_register, font=("Times New Roman", 18), textvariable=self.Email ,bg="white").place(x=260,
                                                                                                            y=270,
                                                                                                            height=25, width=220)
                                            #CREDITCARD NUMBER
        label = Label(frame_register, text="CreditCardno", font=("Times New Roman", 18),
                      bg="white").place(x=20, y=310)
        entry = Entry(frame_register, textvariable=self.Creditcardno, font=("Times New Roman", 18), bg="white").place(
            x=260, y=310,height=25, width=220)
                                                #USERNAME
        label = Label(frame_register, text="Username", font=("Times New Roman", 18), bg="white").place(x=20, y=350,
                                                                                                       )
        entry = Entry(frame_register, font=("Times New Roman", 18), textvariable=self.Username, bg="white").place(x=260,
                                                                                                               y=350,
                                                                                                             height=25, width=220)
                                             #PASSWORD
        label = Label(frame_register, text="Password", font=("Times New Roman", 18), bg="white").place(x=20, y=390,
                                                                                                       )
        entry = Entry(frame_register, font=("Times New Roman", 18), show="*", textvariable=self.Password,
                      bg="white").place(x=260, y=390, height=25, width=220)
                                        #CONFIRM PASSWORD
        label = Label(frame_register, text="Confirm Password", font=("Times New Roman", 18), bg="white").place(x=20,
                                                                                                               y=430,
                                                                                                              )
        entry = Entry(frame_register, font=("Times New Roman", 18), show="*", textvariable=self.Confirmpassword,
                      bg="white").place(x=260, y=430,height=25, width=220)
                                        #SECURITY QUESTION
        question = Label(frame_register, text="Security Question", font=("Times New Roman", 18),bg= "white", fg="orange").place(x=20, y=470,
                                                                                                       )
        self.cmb_quest = ttk.Combobox(frame_register, font=("Times New Roman", 18))
        self.cmb_quest['values'] = ("Select", "Your Favourite Pet Name", "Your Birthplace", "Your Best Friend Name")
        self.cmb_quest.place(x=260, y=470, height=25, width=220)
        self.cmb_quest.current(0)
                                          #ANSWER
        answer = Label(frame_register, text="Answer", font=("Times New Roman", 18), bg="white").place(x=20, y=500)
        entry = Entry(frame_register, font=("Times New Roman", 18), textvariable=self.securityanswer, bg="white").place(
            x=260, y=500, height=25, width=220)

                                       #AGREE CHECK BUTTON
        check = Checkbutton(frame_register, onvalue=1, offvalue=0,
                            text="By checking this box you agree to all the terms and conditions ",
                            variable=self.var_chk).place(x=90, y=540, height=30)

                                   #REGISTER AND LOGIN BUTTON
        button = Button(frame_register, text="SignUp", command=self.registerFunc, font=("times new roman", 18, "bold"), bg="orange").place(x=210, y=580, width=100, height=40)
        button = Button(frame_register, text="SignIn", command=self.Log, font=("times new roman", 18, "bold"),
                        bg="orange").place(x=300, y=580, width=100, height=40)

                                              #DATABASE

        name1=self.Firstname.get()
        name2=self.Lastname.get()
        gender=self.Gender.get()
        address=self.Address.get()
        phonenumber=self.Phonenumber.get()
        email=self.Email.get()
        creditcardno=self.Creditcardno.get()
        username=self.Username.get()
        password=self.Password.get()
        confirmpassword=self.Confirmpassword.get()



                                     #DATABASE USING MYSQL#
        #VALIDATION RULES #


    def registerFunc(self):
        # pat = "^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        # # # SpecialSym = ['0-9']
        # # # if self.Firstname.get()<=8 or self.Lastname.get()<=8 or self.Username.get()<=8:
        # # #     messagebox.showinfo("Error", "Invalid Name", parent=self.root)
        #
        # # # if self.Gender.get()>=4:
        # # #     messagebox.showinfo("Error", "Choose Mr., Mrs. or  Ms", parent=self.root)
        # # # if self.Address.get()<=8:
        # # #     messagebox.showinfo("Error", "Invalid Address", parent=self.root)
        # # # if self.Password.get() !=SpecialSym:
        # # #     messagebox.showinfo("Error","Create another password", parent=self.root)
        # #
        # #
        # if self.Email.get()!=pat :
        #     messagebox.showerror("Error Message","Invalid Email", parent=self.root)
        # elif self.Phonenumber.get()<=9 or self.Phonenumber.get()<9:
        #     messagebox.showerror("Error", "Invalid Phone Number", parent=self.root)
        if  self.Password.get() != self.Confirmpassword.get():
            messagebox.showinfo("Message", "Mismatch Password", parent=self.root)
        if self.var_chk.get() == 0:
            messagebox.showerror("Error","Please agree to our terms and condition", parent=self.root)
        if self.Firstname.get()=="" or  self.Lastname.get()=="" or self.Gender.get()=="" or self.Address.get()=="" or self.Phonenumber.get()=="" or self.Email.get()=="" or self.Creditcardno.get()=="" or self.Username.get()=="" or  self.Password.get()=="" or self.Confirmpassword.get()=="":
            messagebox.showerror("Error","Please fill all the details", parent=self.root)
        if self.securityanswer.get()=="" :
            messagebox.showerror("Message","Invalid security answer", parent=self.root)
        # elif self.Creditcardno.get()<=16 or self.Creditcardno.get()>=16:
        #     messagebox.showerror("Error", "Invalid Credit Card Number", parent=self.root)

        else:
            try:
                con = mysql.connector.connect(host="localhost", user="root", password="",
                                              database="taxibookingsystem")
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO Register ( first_name, last_name, gender, address, phone_number, cemail, credit_card_no, username, passwords, confirm_passwords,question, security_answer) values( %s,%s, %s,%s, %s,%s, %s,%s, %s,%s,%s,%s)",
                    (self.Firstname.get(),
                     self.Lastname.get(),
                     self.Gender.get(),
                     self.Address.get(),
                     self.Phonenumber.get(),
                     self.Email.get(),
                     self.Creditcardno.get(),
                     self.Username.get(),
                     self.Password.get(),
                     self.Confirmpassword.get(),
                     self.cmb_quest.get(),
                     self.securityanswer.get()

                     ))
                con.commit()
                con.close()
                messagebox.showwarning("SUCCESS","Registration successful", parent=self.root)
                self.clearFunc()
            except Exception as ex:
                messagebox.showerror("Message", f"Error due to : {str(ex)}", parent=self.root)

    def clearFunc(self):
        self.Firstname.set(""),
        self.Lastname.set(""),
        self.Gender.set(""),
        self.Address.set(""),
        self.Phonenumber.set(""),
        self.Email.set(""),
        self.Creditcardno.set(""),
        self.Username.set(""),
        self.Password.set(""),
        self.Confirmpassword.set(""),
        self.securityanswer.set("")

    def Log(self):
        self.root.destroy()
        self.new_obj = mainloginClass()

#
# if __name__ == "__main__":
#     obj = registerClass()
#     mainloop()