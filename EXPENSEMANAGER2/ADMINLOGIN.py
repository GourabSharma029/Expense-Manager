from tkinter import *
import tkinter.messagebox as msg
from connect import connect
import admindashboard

class main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Admin Login")
        self.root.state('zoomed')
        self.root.config(bg="DodgerBlue2")
        self.mainLabel = Label(self.root, text="Admin Login", font=('calibri', 30, 'bold', 'underline'))
        self.mainLabel.pack(pady=20)
        frame_login = Frame(self.root, bg="white", width=500, height=400)
        frame_login.place(x=500, y=200)
        title = Label(frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="blue", bg="white").place(x=120,
                                                                                                                y=30)
        subtitle = Label(frame_login, text="Admin Login Area", font=("Gaudy old style", 15, "bold"), fg="black",
                         bg="white").place(x=120, y=100)
        self.lbl_username = Label(frame_login, text="Enter email", font=("Gaudy old style", 15, "bold"), fg="grey",
                                  bg="white").place(x=50, y=160)
        self.txt1 = Entry(frame_login, font=("Gaudy old style", 15), bg="white")
        self.txt1.place(x=50, y=190, width=320, height=35)
        self.lbl_password = Label(frame_login, text="Password", font=("Gaudy old style", 15, "bold"), fg="grey",
                                  bg="white").place(x=50, y=250)
        self.txt2 = Entry(frame_login, show='*', font=("Gaudy old style", 15), bg="white")
        self.txt2.place(x=50, y=280, width=320, height=35)
        button = Button(frame_login, text="Submit",command=self.checkAdmin, font=("Impact", 15), fg="white",
                        cursor='hand2', bg="blue").place(x=50, y=330, width=150, height=30)

        self.root.mainloop()

    def checkAdmin(self):
        self.email = self.txt1.get()
        self.password = self.txt2.get()
        if self.email == "" or self.password == "":
            msg.showerror("Error", "All Fields Are Required", parent=self.root)
        else:

            conn = connect()
            cr = conn.cursor()
            q1 = f"select * from admin where email='{self.email}' and password='{self.password}'"
            cr.execute(q1)
            result = cr.fetchone()
            if result is None:
                msg.showerror("Error", "Invalid Email/Password", parent=self.root)
            else:
                msg.showinfo("", "Login Successful")
                self.root.destroy()
                admindashboard.dashboard()


