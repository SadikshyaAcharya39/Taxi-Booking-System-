################ IMPORTING REQUIRED MODULES #########
import pathlib
from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
from mysql.connector.errors import DatabaseError
import PIL
from PIL import ImageTk, Image  # pip install pillow

#
new_path = pathlib.Path('.') / 't1.jpg'
# print(new_path)
import time

from tkcalendar import Calendar, DateEntry


# def globalIni(self,email):
#     global pri_email
#     pri_email = email
#     self.show()

############# CLASS CREATED #######
######### BOOKING PAGE MADE ##########
class bookingClass():
    def __init__(self, level, email):
        self.level = level
        self.email = email
        self.root = None
        self.booking()

    def booking(self):
        self.root = Tk()
        self.root.geometry('1350x718')
        self.root.title("Sadikshya Acharya|| TAXI BOOKING SYSTEM")
        self.root.state('zoomed')
        self.root.configure(background="orange")
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
        self.call()
        self.heading = Label(self.root, text=username, font=('Times New Roman', 15, 'bold'), bg='orange',
                             fg='white')
        self.heading.place(x=1100, y=0, width=150, height=40)

        # frame for booking
        frame_booking = Frame(self.root, bg="white")
        frame_booking.place(x=20, y=45, height=570, width=480)

        ##########VARIABLE DECLARATION #############
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
        self.var_creditcard_number = StringVar()
        self.var_booking_status = StringVar()
        self.var_driver_name = StringVar()
        self.var_driver_license_plate = StringVar()

        # title
        title = Label(frame_booking, text="Booking Page", font=("Times New Roman", 20, "bold"), bg="orange", fg="white")
        title.place(x=140, y=10)

        # label and entry
        label2 = Label(frame_booking, text="Customer Name", font=("Times New Roman", 18), bg="white").place(x=20, y=90,
                                                                                                            )
        entry2 = Entry(frame_booking, textvariable=self.var_customer_name, font=("Times New Roman", 18),
                       bg="white").place(
            x=240, y=90, height=25, width=220)

        # label3 = Label(frame_booking, text="Gender", font=("Times New Roman", 18), bg="white").place(x=20, y=130,
        #                                                                                                     )
        # entry3 = Entry(frame_booking, textvariable=self.var_gender, font=("Times New Roman", 18),
        #                bg="white").place(
        #     x=240, y=130, height=25, width=220)
        label4 = Label(frame_booking, text="Booking Date", font=("Times New Roman", 18), bg="white").place(x=20, y=130,
                                                                                                           )
        entry4 = DateEntry(frame_booking, textvariable=self.var_booking_date, font=("Times New Roman", 18),
                           bg="white").place(
            x=240, y=130, height=25, width=220)

        label5 = Label(frame_booking, text="Pickup Date", font=("Times New Roman", 18), bg="white").place(x=20, y=170,
                                                                                                          )
        entry5 = DateEntry(frame_booking, textvariable=self.var_pickup_date, font=("Times New Roman", 18),
                           bg="white").place(
            x=240, y=170, height=25, width=220)

        label6 = Label(frame_booking, text="Pickup Time ", font=("Times New Roman", 18), bg="white").place(x=20, y=210,
                                                                                                           )
        entry6 = Entry(frame_booking, textvariable=self.var_pickup_time, font=("Times new Roman", 18),
                       bg="white").place(
            x=240, y=210, height=25, width=220)

        label7 = Label(frame_booking, text="Pickup Address", font=("Times New Roman", 18), bg="white").place(x=20,
                                                                                                             y=250,
                                                                                                             )
        entry7 = Entry(frame_booking, textvariable=self.var_pickup_address, font=("Times new Roman", 18),
                       bg="white").place(x=240, y=250, height=25, width=220)

        label8 = Label(frame_booking, text="Dropoff Date", font=("Times New Roman", 18), bg="white").place(x=20, y=290,
                                                                                                           )
        entry8 = DateEntry(frame_booking, textvariable=self.var_dropoff_date, font=("Times New Roman", 18),
                           bg="white").place(
            x=240, y=290, height=25, width=220)

        label9 = Label(frame_booking, text="Dropoff Destination", font=("Times New Roman", 18), bg="white").place(x=20,
                                                                                                                  y=330,
                                                                                                                  )
        entry9 = Entry(frame_booking, textvariable=self.var_dropoff_destination, font=("Times New Roman", 18),
                       bg="white").place(x=240, y=330, height=25, width=220)

        label10 = Label(frame_booking, text="No. of cars required", font=("Times new Roman", 18), bg="white").place(
            x=20, y=370)
        entry10 = Entry(frame_booking, textvariable=self.var_no_of_car_required, font=("Times New Roman", 18),
                        bg="white").place(x=240, y=370, height=25, width=220)

        label11 = Label(frame_booking, text="Creditcard number", font=("Times New Roman", 18), bg="white").place(x=20,
                                                                                                                 y=410,
                                                                                                                 )
        entry11 = Entry(frame_booking, textvariable=self.var_creditcard_number, font=("Times New Roman", 18),
                        bg="white").place(x=240, y=410, height=25, width=220)

        ######### BUTTON TO BOOK TAXI
        booking_Button = Button(frame_booking, text=" Book Now ", command=self.book, font=("Times new Roman", 12),
                                bg="orange", fg="white")
        booking_Button.place(x=30, y=470)

        ###### TO VIEW CONFIRMED BOOKING
        view_Button = Button(frame_booking, text="Confirm Booking ", command=self.viewconfirm,
                             font=("Times New Roman", 12),
                             bg="orange", fg="white")
        view_Button.place(x=130, y=470)
        #### CANCEL BOOKING
        cancel_Button = Button(frame_booking, text="Cancel Booking ", command=self.delete, font=("Times New Roman", 12),
                               bg="orange", fg="white")
        cancel_Button.place(x=260, y=470)
        #
        clear_Button = Button(frame_booking, text="Clear ", command=self.clear, font=("Times New Roman", 12),
                              bg="orange", fg="white")
        clear_Button.place(x=380, y=470)

        ####### LOG OUT BUTTON
        cancel_Button = Button(frame_booking, text="Log out ", command=exit, font=("Times New Roman", 12),
                               bg="orange", fg="white")
        cancel_Button.place(x=220, y=510)

        # showing details
        # frame
        frame_view = Frame(self.root, bg="white")
        frame_view.place(x=530, y=45, height=570, width=740)

        # # title
        # title = Label(frame_view, text="Your Booking Details", font=("Times New Roman", 20, "bold"), bg="white")
        # title.place(x=120, y=15)

        # scroollbar
        scrolly = Scrollbar(frame_view, orient=VERTICAL)
        scrollx = Scrollbar(frame_view, orient=HORIZONTAL)
        # "customer_name",

        # create tables
        self.booking_Table = ttk.Treeview(frame_view, columns=(
            "booking_id", "customer_name", "booking_date", "pickup_date", "pickup_time", "pickup_address",
            "dropoff_date",
            "dropoff_destination", "no_of_car_required", "creditcard_number", "booking_status"),
                                          yscrollcommand=scrolly.set,
                                          xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.booking_Table.xview)
        scrolly.config(command=self.booking_Table.yview)

        self.booking_Table.heading("booking_id", text="Booking ID")
        self.booking_Table.heading("customer_name", text="Customer Name")
        # self.booking_Table.heading("gender", text="Gender")
        self.booking_Table.heading("booking_date", text="Booking Date")
        self.booking_Table.heading("pickup_date", text="Pickup Date")
        self.booking_Table.heading("pickup_time", text="Pickup Time")
        self.booking_Table.heading("pickup_address", text="Pickup Address")
        self.booking_Table.heading("dropoff_date", text="Dropoff Date")
        self.booking_Table.heading("dropoff_destination", text="Dropoff Destination")
        self.booking_Table.heading("no_of_car_required", text="No of cars required")
        self.booking_Table.heading("creditcard_number", text="Creditcard Number")
        self.booking_Table.heading("booking_status", text="Booking Status")

        self.booking_Table["show"] = "headings"
        self.booking_Table.column("booking_id", width=70)
        self.booking_Table.column("customer_name", width=95)
        # self.booking_Table.column("gender", width=95)
        self.booking_Table.column("booking_date", width=85)
        self.booking_Table.column("pickup_date", width=75)
        self.booking_Table.column("pickup_time", width=75)
        self.booking_Table.column("pickup_address", width=90)
        self.booking_Table.column("dropoff_date", width=77)
        self.booking_Table.column("dropoff_destination", width=115)
        self.booking_Table.column("no_of_car_required", width=120)
        self.booking_Table.column("creditcard_number", width=120)
        self.booking_Table.column("booking_status", width=120)

        self.booking_Table.pack(fill=BOTH, expand=1)
        self.booking_Table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

        ########showdata
        self.root.mainloop()


    def show(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
        cur = con.cursor()
        try:
            cur.execute(
                "select * from register where cemail=%s ",(self.email,))
            rows = cur.fetchone()
            user = rows[0]

            global useremail
            useremail = user




            cur.execute(
                "select  booking_id, customer_name,booking_date, pickup_date, pickup_time, pickup_address, dropoff_date, dropoff_destination, no_of_car_required, creditcard_number, booking_status from Booking where cemail=%s",(user,))
            rows = cur.fetchall()
            self.booking_Table.delete(*self.booking_Table.get_children())
            for row in rows:
                self.booking_Table.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

        ################ TO GET DATAS IN ENTRY

    def get_data(self, ev):
        f = self.booking_Table.focus()
        content = (self.booking_Table.item(f))
        row = content['values']
        self.var_booking_id.set([0]),
        self.var_customer_name.set(row[1]),
        # self.var_gender.set(row[2]),
        self.var_booking_date.set(row[2]),
        self.var_pickup_date.set(row[3]),
        self.var_pickup_time.set(row[4]),
        self.var_pickup_address.set(row[5]),
        self.var_dropoff_date.set(row[6]),
        self.var_dropoff_destination.set(row[7]),
        self.var_no_of_car_required.set(row[8]),
        self.var_creditcard_number.set(row[9]),
        self.var_booking_status.set(row[10]),

        ###################book
        ######## DATABASE CONNECTION #################

    def book(self):
        # if self.var_booking_date>=self.var_pickup_date or self.var_pickup_date>=self.var_dropoff_date:
        #     messagebox.showerror("Error","Invalid date")

        con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
        cur = con.cursor()
        cur.execute(
            "INSERT INTO Booking (customer_name,booking_date, pickup_date, pickup_time, pickup_address, dropoff_date, dropoff_destination, no_of_car_required, creditcard_number, booking_status,cemail) values( %s,%s,%s,%s,%s,%s,%s,%s,%s,'Pending',%s)",
            (self.var_customer_name.get(),

             self.var_booking_date.get(),
             self.var_pickup_date.get(),
             self.var_pickup_time.get(),
             self.var_pickup_address.get(),
             self.var_dropoff_date.get(),
             self.var_dropoff_destination.get(),
             self.var_no_of_car_required.get(),
             self.var_creditcard_number.get(),
             useremail
             ))
        con.commit()
        messagebox.showinfo("Success", "Congratulations! Booking is  done successfully", parent=self.root)
        self.show()
        con.close()
    def call(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
        cur = con.cursor()
        try:
            cur.execute(
                "select  * from register where cemail=%s ", (self.email,))
            rows = cur.fetchone()
            user = rows[0]
            name = rows[1]
            global useremail
            useremail = user

            global username
            username = name
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)
    # def update(self):
    #     con=mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
    #     cur=con.cursor()
    #     cur.execute("UPDATE Booking SET customer_name=?,gender=? ,booking_date=?, pickup_date=?, pickup_time=?, pickup_address=?, dropoff_date=?, dropoff_destination=?, no_of_car_required=?, creditcard_number=? WHERE booking_id = ?",
    #                 (
    #                  self.var_customer_name.get(),
    #                  self.var_gender.get(),
    #                  self.var_booking_date.get(),
    #                  self.var_pickup_date.get(),
    #                  self.var_pickup_time.get(),
    #                  self.var_pickup_address.get(),
    #                  self.var_dropoff_date.get(),
    #                  self.var_dropoff_destination.get(),
    #                  self.var_no_of_car_required.get(),
    #                  self.var_creditcard_number.get()
    #                 ))
    #     con.commit()
    #     messagebox.showinfo("success", "your data is updated", parent=self.root)
    #     con.close()

    ################### DELETE BOOKINGS ##############
    def delete(self):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
            cur = con.cursor()
            op = messagebox.askyesno("Confirm", "Do you want to delete?", parent=self.root)

            selected_item = self.booking_Table.selection()[0]
            book_id = self.booking_Table.item(selected_item)['values'][0]
            # print(book_id)
            if op == True:
                cur.execute("delete from Booking where booking_id = %s ", (book_id,))
                con.commit()
                messagebox.showinfo("Booking deleted Successfully", parent=self.root)
                self.clear()
                self.show()
        except Exception as es:
            messagebox.showerror("Error", f"Error due to : {str(es)}")

    #################clear
    def clear(self):
        self.var_customer_name.set(""),

        self.var_booking_date.set(""),
        self.var_pickup_date.set(""),
        self.var_pickup_time.set(""),
        self.var_pickup_address.set(""),
        self.var_dropoff_date.set(""),
        self.var_dropoff_destination.set(""),
        self.var_no_of_car_required.set(""),
        self.var_creditcard_number.set("")

    #     ################ VIEW BOOKING #############
    #
    def viewconfirm(self):
        self.root2 = Toplevel()
        self.root.title("Sadikshya Acharya|| TAXI BOOKING SYSTEM")
        self.root2.geometry("1350x718")
        # self.root2.focus_force()
        self.root.state('zoomed')
        self.root.resizable(False, False)
        self.root.configure(background="orange")

        # # Image #
        # image = PIL.Image.open('t1.jpg').resize((int(self.root.winfo_screenwidth()),
        #                                          int(self.root.winfo_screenheight())))
        # self.bg = ImageTk.PhotoImage(image)
        # self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0)

        # showing details
        # frame
        frame_view = Frame(self.root2, bg="white")
        frame_view.place(x=30, y=100, height=500, width=1230)

        # title
        title = Label(frame_view, text="Your Confirm Booking Details", font=("Times New Roman", 20, "bold"), bg="white",
                      fg="orange")
        title.place(x=150, y=20)

        # scroollbar
        scrolly = Scrollbar(frame_view, orient=VERTICAL)
        scrollx = Scrollbar(frame_view, orient=HORIZONTAL)

        # create tables
        # "gender",
        self.admin_Table = ttk.Treeview(frame_view, columns=(
            "bookingconfirmation_id", "customer_name", "booking_date", "pickup_date", "pickup_time",
            "pickup_address", "dropoff_date", "dropoff_destination", "no_of_car_required", "driver_name",
            "driver_license_plate", "booking_status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.admin_Table.xview)
        scrolly.config(command=self.admin_Table.yview)

        # heading

        self.admin_Table.heading("bookingconfirmation_id", text="confirmation ID")
        self.admin_Table.heading("customer_name", text="Customer Name")
        # self.admin_Table.heading("gender", text="Gender")
        self.admin_Table.heading("booking_date", text="Booking date")
        self.admin_Table.heading("pickup_date", text="Pickup date")
        self.admin_Table.heading("pickup_time", text="Pickup time")
        self.admin_Table.heading("pickup_address", text="Pickup address")
        self.admin_Table.heading("dropoff_date", text="Dropoff date")
        self.admin_Table.heading("dropoff_destination", text="Dropoff destination")
        self.admin_Table.heading("no_of_car_required", text="No of cars required")
        self.admin_Table.heading("driver_name", text="driver name")
        self.admin_Table.heading("driver_license_plate", text="driver licence plate")
        self.admin_Table.heading("booking_status", text="booking_status")

        self.admin_Table["show"] = "headings"

        self.admin_Table.column("bookingconfirmation_id", width=100)
        self.admin_Table.column("customer_name", width=100)
        # self.admin_Table.column("gender", width=100)
        self.admin_Table.column("booking_date", width=100)
        self.admin_Table.column("pickup_date", width=100)
        self.admin_Table.column("pickup_time", width=100)
        self.admin_Table.column("pickup_address", width=100)
        self.admin_Table.column("dropoff_date", width=100)
        self.admin_Table.column("dropoff_destination", width=100)
        self.admin_Table.column("no_of_car_required", width=100)
        self.admin_Table.column("driver_name", width=100)
        self.admin_Table.column("driver_license_plate", width=100)
        self.admin_Table.column("booking_status", width=100)

        self.admin_Table.pack(fill=BOTH, expand=1)
        self.admin_Table.bind("<ButtonRelease-1>", self.get_data1)
        self.show1()

        ############### CONFIRM BOOKING ############

    def show1(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
        cur = con.cursor()
        try:
            cur.execute(
                "select b.booking_id,b.customer_name,b.booking_date,b.pickup_date,b.pickup_time,b.pickup_address,b.dropoff_date,b.dropoff_destination,b.no_of_car_required,b.booking_status ,d.driver_name,d.driver_license_plate from Booking b inner join taxi_driver d on b.cemail = d.email")
            rows = cur.fetchall()
            self.admin_Table.delete(*self.admin_Table.get_children())
            for row in rows:
                self.admin_Table.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    #
    def get_data1(self, ev):
        f = self.admin_Table.focus()
        content = (self.admin_Table.item(f))
        row = content['values']
        self.var_admin_id.set(row[0]),
        self.var_booking_id.set(row[1]),
        self.var_customer_name.set(row[2]),
        self.var_booking_date.set(row[3]),
        self.var_pickup_date.set(row[4]),
        self.var_pickup_time.set(row[5]),
        self.var_pickup_address.set(row[6]),
        self.var_dropoff_date.set(row[7]),
        self.var_dropoff_destination.set(row[8]),
        self.var_no_of_car_required.set(row[9]),
        self.var_driver_name.set(row[10]),
        self.var_driver_license_plate.set(row[11]),
        self.var_booking_status.set(row[12]),

# if __name__ == "__main__":
#     obj = bookingClass()
#     mainloop()
