from tkinter import *
import tkinter.messagebox as msg
from connect import connect
import addbudget1
import tkcalendar
import tkinter.ttk as ttk
import datetime
import changepassuser
import viewgraph


class dashboard:
    def __init__(self, user):
        self.root = Tk()
        self.root.title("USER Dashboard")
        self.root.state('zoomed')
        self.root.config(bg="Dodgerblue3")

        self.rootMenu = Menu(self.root)
        self.root.config(menu=self.rootMenu)

        self.profileMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label="Profile", menu=self.profileMenu)
        self.profileMenu.add_command(label="Change Password",command=changepassuser.change)
        self.profileMenu.add_command(label="Logout", command=lambda: self.root.destroy())

        self.rootMenu.add_command(label="Add Budget", command=lambda: addbudget1.main(userid=user[0]))

        self.conn = connect()
        self.cr = self.conn.cursor()

        self.mainLabel = Label(self.root, text=f"Welcome {user[1]}", font=('calibri', 30, 'bold', 'underline'))
        self.mainLabel.pack(pady=20)

        self.f1 = Frame(self.root)
        self.f1.pack()

        self.lb11 = Label(self.f1, text=f"Total Budget ->  {0}", font=('arial', 26, 'bold'))
        self.lb11.grid(row=0, column=0, pady=20, padx=20)

        self.lb12 = Label(self.f1, text=f"Total Expences ->  {0}", font=('arial', 26, 'bold'))
        self.lb12.grid(row=0, column=1, pady=20, padx=20)

        self.lb13 = Label(self.f1, text=f"Remaining Budget ->  {0}", font=('arial', 26, 'bold'))
        self.lb13.grid(row=0, column=2, pady=20, padx=20)

        self.frame = Frame(self.root)
        self.frame.pack(pady=40)

        self.lb1 = Label(self.frame, text="Select Date")
        self.lb1.grid(row=0, column=0)

        self.txt1 = tkcalendar.DateEntry(self.frame, width=37)
        self.txt1.grid(row=0, column=1)

        self.lb2 = Label(self.frame, text="Amount")
        self.lb2.grid(row=0, column=2)

        self.txt2 = Entry(self.frame, width=40)
        self.txt2.grid(row=0, column=3)

        cat = self.getCategories()
        self.lb3 = Label(self.frame, text="Category")
        self.lb3.grid(row=0, column=4)

        self.txt3 = ttk.Combobox(self.frame, width=37, state='readonly', values=cat)
        self.txt3.grid(row=0, column=5)

        self.userid = user[0]

        self.btn = Button(self.frame, text="Submit", command=self.addExpence)
        self.btn.grid(row=0, column=6)


        self.btn = Button(self.frame, text="View Graph", command=self.view)
        self.btn.grid(row=0, column=7)



        col = ["id", "date", 'amount', 'category']
        self.tv = ttk.Treeview(self.root, columns=col)
        self.tv.pack(pady=20)
        for i in col:
            self.tv.heading(i, text=i.capitalize())
        self.tv['show'] = 'headings'
        self.getValues()
        self.getBudget()
        self.root.mainloop()

    def view(self):
            a = self.userid
            viewgraph.main(a)

    def getValues(self):
        q = f"select id,date,amount,category from expense where userid='{self.userid}'"
        self.cr.execute(q)

        result = self.cr.fetchall()

        for j in self.tv.get_children():
            self.tv.delete(j)

        for i in range(0, len(result)):
            self.tv.insert("",index=i,values=list(result[i]))



    def addExpence(self):
        self.date = self.changeDateFormat(self.txt1.get())
        self.amount = self.txt2.get()
        self.category = self.txt3.get()
        option = True
        if float(self.amount) > self.remainingBudget:
            option = msg.askyesno("", "Your Budget has been Exceeded! Still want to add new Expence?",parent=self.root)
        if len(self.date) == 0 or len(self.amount) == 0 or len(self.category) == 0:
            msg.showwarning("", "PLease input all fields", parent=self.root)
        else:
            if option is True:
                q = f"insert into expense values(NULL, '{self.userid}', '{self.date}','{self.amount}','{self.category}')"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo("", "Expence Added Successfully",parent=self.root)
                self.getBudget()
                self.getValues()
            else:
                msg.showinfo("", "Your Budget Remains Same",parent=self.root)
            self.txt2.delete(0, "end")
            self.txt3.set('')

    def getBudget(self):
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
        d = {1: "January", 2: "Febuary", 3: "March", 4: 'April', 5: "May", 6: 'June',
             7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November',
             12: 'December'}
        self.conn = connect()
        self.cr = self.conn.cursor()

        q = f"select amount from budget where userid='{self.userid}' and month ='{d[month]}'" \
            f"and year='{year}'"
        self.cr.execute(q)
        result = self.cr.fetchone()
        print(result)
        self.totalBudget = result[0]
        newMonth = ""
        if len(str(month)) == 1:
            newMonth = f"0{month}"
        q1 = f"select date,amount from expense where userid='{self.userid}'"
        self.cr.execute(q1)
        alldata = self.cr.fetchall()

        print(alldata)
        self.totalExpence = 0
        for i in alldata:
                self.totalExpence = self.totalExpence +i[1]

        print(self.totalExpence)

        self.remainingBudget = self.totalBudget - self.totalExpence
        self.lb11.config(text=f"Total Budget ->  {self.totalBudget}")
        self.lb12.config(text=f"Total Expence ->  {self.totalExpence}")
        self.lb13.config(text=f"Remaining Budget ->  {self.remainingBudget}")


    def getCategories(self):
        q = "select * from category"
        self.cr.execute(q)
        result = self.cr.fetchall()
        # print(result)
        data = []
        for i in result:
            data.append(i[0])
        return data


    def changeDateFormat(self, date):
        date_lst = str(date).split('/')
        new_date_st = ""
        new_date_st = new_date_st + "20" + date_lst[2] + "-"

        if len(date_lst[0]) == 1:
            new_date_st = new_date_st + "0" + date_lst[0] + "-"
        else:
            new_date_st = new_date_st + date_lst[0] + "-"

        if len(date_lst[1]) == 1:
            new_date_st = new_date_st + "0" + date_lst[1]
        else:
            new_date_st = new_date_st + date_lst[1] + "-"
        # print(new_date_st)
        return new_date_st

