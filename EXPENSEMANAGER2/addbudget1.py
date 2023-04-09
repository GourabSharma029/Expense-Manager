from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connect import connect

class main:
    def __init__(self, userid):
        self.root = Tk()
        self.root.title("Add Budget")
        self.root.state('zoomed')
        self.root.config(bg="SteelBlue1")

        self.mainLabel = Label(self.root, text="Add Budget", font=('calibri', 30, 'bold', 'underline'))
        self.mainLabel.pack(pady=20)
        self.userid = userid
        self.Frame1 = Frame(self.root, bg="white", width=500, height=500)
        self.Frame1.place(x=500, y=180)

        title = Label(self.Frame1, text="Add Budget Here", font=("Impact", 35, "bold"), fg="blue", bg="white").place(
            x=120, y=30)

        self.lb1 = Label(self.Frame1, text="Enter Amount", font=("Gaudy old style", 15, "bold"), fg="grey",
                         bg="white").place(x=50, y=160)
        self.txt1 = Entry(self.Frame1, font=("Gaudy old style", 15), bg="white")
        self.txt1.place(x=50, y=190, width=320, height=35)
        self.lb2 = Label(self.Frame1, text="Enter Month", font=("Gaudy old style", 15, "bold"), fg="grey", bg="white").place(x=50, y=220)
        months = ['January', 'Febuary', 'March', "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.txt2 = ttk.Combobox(self.Frame1, values=months, state='readonly', width=50)
        self.txt2.place(x=50, y=250, width=320, height=35)
        self.lb3 = Label(self.Frame1, text="Enter Year", font=("Gaudy old style", 15, "bold"), fg="grey",  bg="white").place(x=50, y=290)
        year = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']
        self.txt3 = ttk.Combobox(self.Frame1, values=year, state='readonly', width=50)
        self.txt3.place(x=50, y=320, width=320, height=35)
        self.btnb = Button(self.Frame1, text="Submit", command=self.addBudget, font=("Impact", 15), fg="white", cursor='hand2', bg="blue").place(x=50, y=380, width=150, height=30)
        self.root.mainloop()

    def addBudget(self):
        self.amount = self.txt1.get()
        self.month = self.txt2.get()
        self.year = self.txt3.get()

        if len(self.amount) == 0 or len(self.month) == 0 or len(self.year) == 0:
            msg.showwarning("","Please Input all Fields",parent=self.root)
        else:
            conn = connect()
            cr = conn.cursor()
            q1 = f"select * from budget where userid='{self.userid}' and month='{self.month}' and year='{self.year}'"
            cr.execute(q1)
            result = cr.fetchone()
            if result is None:
                q = f"insert into budget values(NULL,'{self.amount}','{self.month}','{self.year}','{self.userid}')"
                cr.execute(q)
                conn.commit()
                msg.showinfo("","Budget addded successfully",parent=self.root)
            else:
                msg.showwarning("","You have already added a budget for this month",parent=self.root)