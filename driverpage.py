###########  IMPORT MODULES ##########
from tkinter import *
import sqlite3
from tkinter import ttk, messagebox

import PIL
import mysql.connector


############ CREATE CLASS ###########
####### DRIVER PAGE CREATED #############
import self
from PIL import ImageTk


class driverpageClass:
    def __init__(self, level, email):
        self.level = level
        self.email = email
        self.root = None
        self.driver()

    def driver(self):
        self.root = Tk()
        self.root.geometry('1350x718')
        self.root.title("Sadikshya Acharya|| TAXI BOOKING SYSTEM")
        self.root.state('zoomed')
        self.root.resizable(False, False)
        self.root.configure(background="orange")
        # # Title(Heading)
        # self.txt = 'Here To There'
        # self.heading = Label(self.root, text=self.txt, font=('Times New Roman', 30, 'bold'), bg='orange',
        #                      fg='white')
        # self.heading.place(x=0, y=0, width=1500, height=40)



        ################ VARIABLE DECLARATION ##############
        self.var_admin_id = StringVar()
        self.var_booking_id = StringVar()
        self.var_customer_name = StringVar()
        self.var_gender = StringVar()
        self.var_booking_date = StringVar()
        self.var_pickup_date = StringVar()
        self.var_pickup_time = StringVar()
        self.var_pickup_address = StringVar()
        self.var_dropoff_date = StringVar()
        self.var_dropoff_destination = StringVar()
        self.var_no_of_car_required = StringVar()
        self.var_driver_name = StringVar()
        self.var_driver_license_plate = StringVar()

        # Title(Heading)

        # label = Label(self.root, text="Welcome To Your Dashboard!!", font=("Times New Roman", 20), fg="red").place(
        #     x=550, y=40)
        # label = Label(self.root, text="List Of All Your Trips", font=("Times New Roman", 20),bg="white", fg="orange").place(x=610, y=80)
        # Image
        image = PIL.Image.open('t1.jpg').resize((int(self.root.winfo_screenwidth()),
                                                 int(self.root.winfo_screenheight())))
        self.bg = ImageTk.PhotoImage(image)
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0)

        # showing details
        # frame
        self.txt = 'Here To There'
        self.heading = Label(self.root, text=self.txt, font=('Times New Roman', 30, 'bold'), bg='orange',
                             fg='white')
        self.heading.place(x=0, y=0, width=1500, height=40)
        label = Label(self.root, text="List Of All Your Trips", font=("Times New Roman", 20), bg="white",
                      fg="orange").place(x=630, y=50)
        ##### LABEL
        self.callname()
        self.heading = Label(self.root, text=drivername, font=('Times New Roman', 15, 'bold'), bg='orange',
                             fg='white')
        self.heading.place(x=1000, y=0, width=230, height=40)
        frame_view = Frame(self.root, bg="white")
        frame_view.place(x=15, y=100, height=500, width=1250)

        foot = LabelFrame(self.root, font=("Times New Roman", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        foot.place(x=220, y=550, width=650, height=50)
        lbl_tl = Label( foot,text="Click on 'Complete Trip' button after completing your Trip.",
                       font=("Times New Roman", 15), bg="white").place(x=10, y=5)
        # ==========================UpdateStatusBtn==============================
        btn_val = Button(foot, text="Complete Trip",command=self.complete, font=("Times New Roman", 15),
                             bg="orange", activebackground="#4caf50", fg="white", activeforeground="white",
                             cursor="hand2").place(x=490, y=10, width=125, height=30)
        if btn_val == 0:
            messagebox.showinfo("Click on complete trip button")

        # scroollbar
        scrolly = Scrollbar(frame_view, orient=VERTICAL)
        scrollx = Scrollbar(frame_view, orient=HORIZONTAL)

        # create tables
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
        self.admin_Table.heading("booking_status", text="Booking Status")

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
        self.admin_Table.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        self.root.mainloop()

    def show(self):
        con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
        cur = con.cursor()
        try:
            cur.execute(
                "select * from taxi_driver where email=%s ", (self.email,))
            rows = cur.fetchone()
            user = rows[0]
            name = rows[1]
            global useremail
            useremail = user

            cur.execute(
                "select b.booking_id,b.customer_name,b.booking_date,b.pickup_date,b.pickup_time,b.pickup_address,b.dropoff_date,b.dropoff_destination,b.no_of_car_required,d.driver_name,d.driver_license_plate, b.booking_status from Booking b inner join taxi_driver d on b.email = d.email where (b.booking_status='OnGoing' or b.booking_status='Completed') and b.email=%s ",(useremail,) )
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
        self.var_admin_id.set(row[0]),
        self.var_booking_id.set(row[1]),
        self.var_customer_name.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_booking_date.set(row[4]),
        self.var_pickup_date.set(row[5]),
        self.var_pickup_time.set(row[6]),
        self.var_pickup_address.set(row[7]),
        self.var_dropoff_date.set(row[8]),
        self.var_dropoff_destination.set(row[9]),
        self.var_no_of_car_required.set(row[10]),
        self.var_driver_name.set(row[11]),
        self.var_driver_license_plate.set(row[12])

    def complete(self):

        selecteditem=self.admin_Table.selection()
        book_id=self.admin_Table.item(selecteditem)['values'][0]
        driver_name = self.admin_Table.item(selecteditem)['values'][9]

        con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
        cur = con.cursor()



        cur.execute("SELECT email from taxi_driver where driver_name=%s", (driver_name,))
        driver_email = cur.fetchone()[0]
        cur.execute("UPDATE taxi_driver set driverstatus='Available' where email=%s", (driver_email,))
        cur.execute("UPDATE booking set booking_status='Completed' where booking_id=%s",(book_id,))
        con.commit()

        messagebox.showinfo("Success", "Your trip is completed!!!")
        self.show()


    def callname(self):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="taxibookingsystem")
            cur = con.cursor()
            cur.execute(
                "select * from taxi_driver where email=%s ", (self.email,))
            rows = cur.fetchone()
            user = rows[0]
            name = rows[1]
            global useremail
            useremail = user

            global drivername
            drivername = name
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

# if __name__ == "__main__":
#     obj = driverpageClass()
#     mainloop()