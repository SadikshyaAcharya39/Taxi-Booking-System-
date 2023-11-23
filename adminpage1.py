# IMPORTING REQUIRED MODULES IMPORTED #
import pathlib
from tkinter import *
import sqlite3
from tkinter import ttk, messagebox

import PIL
import mysql.connector

from tkcalendar import Calendar, DateEntry

# CLASS CREATED #
# ADMIN PAGE CREATED #


import PIL
from PIL import ImageTk, Image  # pip install pillow

#
new_path = pathlib.Path('.') / 't1.jpg'
# print(new_path)


class adminpageClass:
    def __init__(self):
        root = Tk()
        self.root = root
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
        frame_admin = Frame(self.root, bg="white")
        frame_admin.place(x=20, y=45, height=580, width=480)

        # title
        title = Label(frame_admin, text="Admin Page", font=("Times New Roman", 20, "bold"), bg="orange", fg="white")
        title.place(x=140, y=10)

        # VARIABLE DECLARATION
        self.driver_list = []
        self.var_admin_id = StringVar()
        self.var_booking_id = StringVar()
        self.var_customer_name = StringVar()
        # self.var_gender = StringVar()
        self.var_booking_date = StringVar()
        self.var_pickup_date = StringVar()
        self.var_pickup_time = StringVar()
        self.var_pickup_address = StringVar()
        self.var_dropoff_date = StringVar()
        self.var_dropoff_destination = StringVar()
        self.var_no_of_car_required = StringVar()
        self.var_driver_name = StringVar()
        self.var_driver_license_plate = StringVar()


        # LABEL AND ENTRY
        label1 = Label(frame_admin, text="Confirmation ID", font=("Times New Roman", 18), bg="white").place(x=20, y=95,
                                                                                                            )
        entry1 = Entry(frame_admin, textvariable=self.var_booking_id, font=("Times New Roman", 18), bg="white").place(
            x=240, y=95, height=25, width=220)

        label2 = Label(frame_admin, text="Customer Name", font=("Times New Roman", 18), bg="white").place(x=20, y=120,
                                                                                                          )
        entry2 = Entry(frame_admin, textvariable=self.var_customer_name, font=("Times New Roman", 18),
                       bg="white").place(
            x=240, y=120, height=25, width=220)

        # label3 = Label(frame_admin, text="Gender", font=("Times New Roman", 18), bg="white").place(x=20, y=135,
        #                                                                                            )
        # entry3 = Entry(frame_admin, textvariable=self.var_gender, font=("Times New Roman", 18), bg="white").place(x=240, y=135,height=25,width=220)

        label4 = Label(frame_admin, text="Booking Date", font=("Times new Roman", 18), bg="white").place(x=20, y=170,
                                                                                                         )
        entry4 = DateEntry(frame_admin, textvariable=self.var_booking_date, font=("Times New Roman", 18),
                           bg="white").place(
            x=240, y=170, height=25, width=220)

        label5 = Label(frame_admin, text="Pickup Date", font=("Times New Roman", 18), bg="white").place(x=20, y=205,
                                                                                                        )
        entry5 = DateEntry(frame_admin, textvariable=self.var_pickup_date, font=("Times New Roman", 18),
                           bg="white").place(
            x=240, y=205, height=25, width=220)

        label6 = Label(frame_admin, text="Pickup Time ", font=("Times New Roman", 18), bg="white").place(x=20, y=240,
                                                                                                         )
        entry6 = Entry(frame_admin, textvariable=self.var_pickup_time, font=("Times New Roman", 18), bg="white").place(
            x=240, y=240, height=25, width=220)

        label7 = Label(frame_admin, text="Pickup Address", font=("Times New Roman", 18), bg="white").place(x=20, y=275,
                                                                                                           )
        entry7 = Entry(frame_admin, textvariable=self.var_pickup_address, font=("Times New Roman", 18),
                       bg="white").place(
            x=240, y=275, height=25, width=220)

        label8 = Label(frame_admin, text="Dropoff Date", font=("Times New Roman", 18), bg="white").place(x=20, y=310,
                                                                                                         )
        entry8 = DateEntry(frame_admin, textvariable=self.var_dropoff_date, font=("Times New Roman", 18),
                           bg="white").place(
            x=240, y=310, height=25, width=220)

        label9 = Label(frame_admin, text="Dropoff Destination", font=("Times New Roman", 18), bg="white").place(x=20,
                                                                                                                y=350,
                                                                                                                )
        entry9 = Entry(frame_admin, textvariable=self.var_dropoff_destination, font=("Times New Roman", 18),
                       bg="white").place(x=240, y=350, height=25, width=220)

        label10 = Label(frame_admin, text="No. of cars required", font=("Times New Roman", 18), bg="white").place(x=20,
                                                                                                                  y=390,
                                                                                                                  )
        entry10 = Entry(frame_admin, textvariable=self.var_no_of_car_required, font=("Times New Roman", 18),
                        bg="white").place(x=240, y=390, height=25, width=220)

        self.fetch_driver()
        #
        # self.driver_list[]
        label10 = Label(frame_admin, text="Driver's Name", font=("Times New Roman", 18), bg="white").place(x=20,
                                                                                                           y=430, )
        self.tf_driver = ttk.Combobox(frame_admin, font=("times new roman", 15),
                                 values=self.driver_list, state='readonly',textvariable=self.var_driver_name, foreground="black", background="#fff",
                                 justify=CENTER)
        self.tf_driver.place(x=240, y=430, width=220, height=25)

        btnconfirm = Button(frame_admin, text="Confirm", command=self.confirm, font=("Times New Roman", 18),
                            bg="orange", fg="white").place(x=20, y=520, height=30, width=100)
        btn = Button(frame_admin, text="Clear", command=self.clear, font=("Times New Roman", 18), bg="orange",
                     fg="white").place(x=310,
                                       y=520,
                                       height=30,
                                       width=100)

        # BILLING BUTTON
        btn = Button(frame_admin, text="Bill", command=self.bill, font=("Times New Roman", 18), bg="orange",
                     fg="white").place(x=120,
                                       y=520,
                                       height=30,
                                       width=100)
        ####### LOG OUT BUTTON
        cancel_Button = Button(frame_admin, text="Log out ", command=exit, font=("Times New Roman", 12),
                               bg="orange", fg="white")
        cancel_Button.place(x=210, y=520, height=30, width=100)

        # frame
        frame_view = Frame(self.root, bg="white")
        frame_view.place(x=520, y=45, height=600, width=750)

        # scroollbar
        scrolly = Scrollbar(frame_view, orient=VERTICAL)
        scrollx = Scrollbar(frame_view, orient=HORIZONTAL)

        # create tables
        self.admin_Table = ttk.Treeview(frame_view, columns=(
            "bookingconfirmation_id", "customer_name", "booking_date", "pickup_date", "pickup_time",
            "pickup_address", "dropoff_date", "dropoff_destination", "no_of_car_required", "cardno", "email", "booking_status"),
                                        yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.admin_Table.xview)
        scrolly.config(command=self.admin_Table.yview)

        self.admin_Table.heading("bookingconfirmation_id", text="Confirmation ID")
        self.admin_Table.heading("customer_name", text="Customer Name")
        # self.admin_Table.heading("gender", text="Gender")
        self.admin_Table.heading("booking_date", text="Booking Date")
        self.admin_Table.heading("pickup_date", text="Pickup Date")
        self.admin_Table.heading("pickup_time", text="Pickup Time")
        self.admin_Table.heading("pickup_address", text="Pickup Address")
        self.admin_Table.heading("dropoff_date", text="Dropoff Date")
        self.admin_Table.heading("dropoff_destination", text="Dropoff Destination")
        self.admin_Table.heading("no_of_car_required", text="No of cars required")
        self.admin_Table.heading("cardno", text="Credit card no")
        self.admin_Table.heading("email", text="Driver email")
        self.admin_Table.heading("booking_status", text="Booking Status")

        self.admin_Table["show"] = "headings"

        self.admin_Table.column("bookingconfirmation_id", width=95)
        self.admin_Table.column("customer_name", width=100)
        # self.admin_Table.column("gender", width=50)
        self.admin_Table.column("booking_date", width=80)
        self.admin_Table.column("pickup_date", width=75)
        self.admin_Table.column("pickup_time", width=80)
        self.admin_Table.column("pickup_address", width=90)
        self.admin_Table.column("dropoff_date", width=80)
        self.admin_Table.column("dropoff_destination", width=100)
        self.admin_Table.column("no_of_car_required", width=100)
        self.admin_Table.column("cardno", width=100)
        self.admin_Table.column("email", width=100)
        self.admin_Table.column("booking_status", width=100)

        self.admin_Table.pack(fill=BOTH, expand=1)

        # frame_view1 = Frame(self.root, bg="white")
        # frame_view1.place(x=520, y=377, height=300, width=750)
        #
        # # scroollbar
        # scrolly = Scrollbar(frame_view1, orient=VERTICAL)
        # scrollx = Scrollbar(frame_view1, orient=HORIZONTAL)

        # # create tables
        # self.admin_Table2 = ttk.Treeview(frame_view1, columns=(
        #     "admin_id", "bookingconfirmation_id", "customer_name", "booking_date", "pickup_date", "pickup_time",
        #     "pickup_address", "dropoff_date", "dropoff_destination", "no_of_car_required", "driver_name",
        #     "driver_license_plate"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        # scrollx.pack(side=BOTTOM, fill=X)
        # scrolly.pack(side=RIGHT, fill=Y)
        # scrollx.config(command=self.admin_Table2.xview)
        # scrolly.config(command=self.admin_Table2.yview)
        #
        # self.admin_Table2.heading("admin_id", text="Admin ID")
        # self.admin_Table2.heading("bookingconfirmation_id", text="Confirmation ID")
        # self.admin_Table2.heading("customer_name", text="Customer Name")
        # # self.admin_Table.heading("gender", text="Gender")
        # self.admin_Table2.heading("booking_date", text="Booking Date")
        # self.admin_Table2.heading("pickup_date", text="Pickup Date")
        # self.admin_Table2.heading("pickup_time", text="Pickup Time")
        # self.admin_Table2.heading("pickup_address", text="Pickup Address")
        # self.admin_Table2.heading("dropoff_date", text="Dropoff Date")
        # self.admin_Table2.heading("dropoff_destination", text="Dropoff Destination")
        # self.admin_Table2.heading("no_of_car_required", text="No of cars required")
        # self.admin_Table2.heading("driver_name", text="Driver Name")
        # self.admin_Table2.heading("driver_license_plate", text="Driver licence Plate")
        #
        # self.admin_Table2["show"] = "headings"
        # self.admin_Table2.column("admin_id", width=60)
        # self.admin_Table2.column("bookingconfirmation_id", width=95)
        # self.admin_Table2.column("customer_name", width=100)
        # # self.admin_Table.column("gender", width=50)
        # self.admin_Table2.column("booking_date", width=80)
        # self.admin_Table2.column("pickup_date", width=75)
        # self.admin_Table2.column("pickup_time", width=80)
        # self.admin_Table2.column("pickup_address", width=90)
        # self.admin_Table2.column("dropoff_date", width=80)
        # self.admin_Table2.column("dropoff_destination", width=100)
        # self.admin_Table2.column("no_of_car_required", width=100)
        # self.admin_Table2.column("driver_name", width=100)
        # self.admin_Table2.column("driver_license_plate", width=100)

        # self.admin_Table.pack(fill=BOTH, expand=1)

        self.admin_Table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

        # SHOW CONFIRMATION PAGE #

    def show(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
        cur = con.cursor()
        try:
            cur.execute("select * from booking")
            rows = cur.fetchall()
            self.admin_Table.delete(*self.admin_Table.get_children())
            for row in rows:
                self.admin_Table.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.admin_Table.focus()
        content = (self.admin_Table.item(f))
        row = content['values']

        self.var_booking_id.set(row[0]),
        self.var_customer_name.set(row[1]),
        # self.var_gender.set(row[3]),
        self.var_booking_date.set(row[2]),
        self.var_pickup_date.set(row[3]),
        self.var_pickup_time.set(row[4]),
        self.var_pickup_address.set(row[5]),
        self.var_dropoff_date.set(row[6]),
        self.var_dropoff_destination.set(row[7]),
        self.var_no_of_car_required.set(row[8]),
        # self.var_driver_name.set(row[10]),

    def clear(self):
        self.var_booking_id.set(""),
        self.var_customer_name.set("", )
        # self.var_gender.set(""),
        self.var_booking_date.set(""),
        self.var_pickup_date.set(""),
        self.var_pickup_time.set(""),
        self.var_pickup_address.set(""),
        self.var_dropoff_date.set(""),
        self.var_dropoff_destination.set(""),
        self.var_no_of_car_required.set(""),
        self.var_driver_name.set(""),
        self.var_driver_license_plate.set("")

        # database

    # def confirm(self):
    #     # frame
    #     frame_view = Frame(self.root, bg="white")
    #     frame_view.place(x=500, y=30, height=640, width=770)
    #
    #     con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
    #     cur = con.cursor()
    #     cur.execute(
    #         "INSERT INTO Adminpage (bookingconfirmation_id, customer_name,  booking_date, pickup_date, pickup_time, pickup_address, dropoff_date, dropoff_destination, no_of_car_required, driver_name, driver_license_plate) values( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
    #         (self.var_booking_id.get(),
    #          self.var_customer_name.get(),
    #          # self.var_gender.get(),
    #          self.var_booking_date.get(),
    #          self.var_pickup_date.get(),
    #          self.var_pickup_time.get(),
    #          self.var_pickup_address.get(),
    #          self.var_dropoff_date.get(),
    #          self.var_dropoff_destination.get(),
    #          self.var_no_of_car_required.get(),
    #          self.var_driver_name.get(),
    #          self.var_driver_license_plate.get()
    #          ))
    #     con.commit()
    #     messagebox.showinfo("Success", "Congratulations! Booking confirmed!!!", parent=self.root)
    #     con.close()
    #
    #     # frame
    #     frame_view = Frame(self.root, bg="white")
    #     frame_view.place(x=560, y=30, height=640, width=770)
    def confirm(self):
       try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
            cur = con.cursor()
            selected_item=self.admin_Table.selection()
            book_id = self.admin_Table.item(selected_item)['values'][0]
            cur.execute("SELECT email from taxi_driver where driver_name=%s", (self.tf_driver.get(),))
            driver_email=cur.fetchone()[0]
            cur.execute("UPDATE taxi_driver set driverstatus='Not Available' where email=%s", (driver_email,))
            cur.execute(
                "UPDATE booking set booking_status='OnGoing' , email=%s where booking_id=%s", (driver_email, book_id,)
            )
            con.commit()
            messagebox.showinfo("Success", "Congratulations! Booking confirmed!!!")
            con.close()
            self.show()
       except Exception  as ex:
           messagebox.showerror("Message", f"Error due to : {str(ex)}", parent=self.root)


        # FOR BILLING #

    def bill(self):
        self.root = Toplevel()
        self.root.geometry('1350x718')
        self.root.state('zoomed')

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

        frame_billing = Frame(self.root, bg="white")
        frame_billing.place(x=400, y=150, height=420, width=450)

        title = Label(frame_billing, text=" BILLING FORM ", font=("Times New Roman", 20), fg='orange', bg='white')
        title.place(x=160, y=15)

        self.distance = StringVar()
        self.amount = IntVar()
        self.total = IntVar()
        self.name = StringVar()

        label1 = Label(frame_billing, text="Customer Name", bg="white", font=("Times New Roman", 18)).place(x=30, y=60)
        entry1 = Entry(frame_billing, textvariable=self.name, font=("times new roman", 14)).place(x=210, y=60,
                                                                                                  width=200)

        label1 = Label(frame_billing, text="Total miles", bg="white", font=("Times New Roman", 18)).place(x=30,
                                                                                                          y=100)
        entry1 = Entry(frame_billing, textvariable=self.distance, font=("Times New Roman", 14)).place(x=210, y=100,
                                                                                                      width=200)

        label2 = Label(frame_billing, text="Per miles", bg="white", font=("Times New Roman", 18)).place(x=30, y=140)
        entry2 = Entry(frame_billing, textvariable=self.amount, font=("Times New Roman", 14)).place(x=210, y=140,
                                                                                                    width=200)

        btn = Button(frame_billing, command=self.multiply, text="(*)").place(x=300, y=175)

        label1 = Label(frame_billing, text="Total ", bg="white", font=("Times New Roman", 18)).place(x=30, y=210)
        entry3 = Entry(frame_billing, textvariable=self.total, font=("Times New Roman", 14)).place(x=210, y=210,
                                                                                                   width=200)

        label1 = Label(frame_billing, text="Total Amount Of Your Trip Is(in $) ", bg="white",
                       font=("Times New Roman", 18)).place(x=30, y=250)
        entry3 = Entry(frame_billing, textvariable=self.total, font=("Times New Roman", 14)).place(x=210, y=300,
                                                                                                   width=150)

    def multiply(self):

        a = int(self.distance.get())
        b = int(self.amount.get())
        total = a * b
        self.total.set(str(total))
        con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
        cur = con.cursor()
        cur.execute(
            "INSERT INTO Billing (customer_name, distance_travelled, amount_per_miles, total ) values(%s, %s,%s,%s)",
            (self.name.get(),
             self.distance.get(),
             self.amount.get(),
             self.total.get()
             ))
        con.commit()
        messagebox.showinfo("Success", "DONE", parent=self.root)
        con.close()

    def fetch_driver(self):
        # self.driver_list.append("Empty")
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
        cursor = conn.cursor()
        try:
            cursor.execute(
                "Select driver_name from taxi_driver where driverstatus = 'Available'")

            #

            driv = cursor.fetchall()

            if len(driv) > 0:
                del self.driver_list[:]
                # self.driver_list.append("Select")
                for i in driv:
                    self.driver_list.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    # def Assign_Driver(self):
    #     conn = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
    #     cursor = conn.cursor()
    #     selected_item = self.admin_Table.selection()[0]
    #     Booking_ID = self.admin_Table.item(selected_item)['values'][0]
    #     try:
    #         cursor.execute("Select email from taxi_driver where driver_name = %s", (self.var_driver_name.get(),))
    #         email = cursor.fetchone()[0]
    #         print(email)
    #         cursor.execute("Update taxi_driver set driverstatus ='Unavailable' where email =%s", (email,))
    #
    #         cursor.execute("Update booking set email=%s  where booking_id=%s", (email, Booking_ID,))
    #         conn.commit()
    #         messagebox.showinfo("success", "Successfully Driver Assigned!", parent=self.root)
    #         self.show()
    #
    #         self.clear()
    #
    #     except Exception as ex:
    #         messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

#
# if __name__ == "__main__":
#     obj = adminpageClass()
#     mainloop()
