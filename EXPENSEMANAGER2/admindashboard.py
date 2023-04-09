from tkinter import *
import tkinter.messagebox as msg
from connect import connect
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import changepassword

class dashboard:
    def __init__(self):
        self.root1 = Tk()
        self.root1.title("Admin Dashboard")
        self.root1.state('zoomed')

        self.root1.config(bg="Dodgerblue3")

        self.rootMenu = Menu(self.root1)
        self.root1.config(menu=self.rootMenu)

        self.adminMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label="Manage Admins", menu=self.adminMenu)
        self.adminMenu.add_command(label="Add Admin",command=self.newadmin)
        self.adminMenu.add_command(label="View Admin",command=self.viewadmin)

        self.catMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label="Manage Category", menu=self.catMenu)
        self.catMenu.add_command(label="Add Category",command=self.addcat)
        self.catMenu.add_command(label="View Category",command=self.viewcat)

        self.profileMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label="Profile", menu=self.profileMenu)
        self.profileMenu.add_command(label="Change Password",command=changepassword.change)
        self.profileMenu.add_command(label="Logout", command=lambda :self.root1.destroy())

        self.mainLabel = Label(self.root1, text="Welcome Admin", font=('Gaudy old style', 30, 'bold', 'underline'))
        self.mainLabel.grid(row=1,column=3,pady=100)

        self.btnin = Button(self.root1, text="OPERATION ON USER", font=('Gaudy old style', 14), fg="blue",command=self.op_user)
        self.btnin.grid(row=7, column=3, pady=30)

        self.mainLabelA = Label(self.root1, text="RULES FOR ADMIN", font=('Gaudy old style', 15, 'bold'), fg="blue")
        self.mainLabelA.grid(row=2, column=2)
        self.mainLabelB= Label(self.root1, text="1.YOU MUST HAVE TO HELP USER WHERE POSSIBLE", font=('Gaudy old style', 14))
        self.mainLabelB.grid(row=3, column=2)
        self.mainLabelC = Label(self.root1, text="2.DONOT MISUSE UR RIGHTS", font=('Gaudy old style', 14))
        self.mainLabelC.grid(row=4, column=2)
        self.mainLabelD = Label(self.root1, text="3.IF ANY PROBLEM FOUND IN UR ACCOUNT U MAY REMOVE", font=('Gaudy old style', 14))
        self.mainLabelD.grid(row=5, column=2)

    def op_user(self):
        self.userop = Toplevel()

        self.userop.geometry("1200x1200")
        self.userop.title("Operation on user")
        self.userop.config(bg="steelblue1")
        self.key = StringVar()
        self.namea=StringVar()
        self.emaila=StringVar()
        self.mobilea = StringVar()
        self.passworda = StringVar()


        self.label1 = Label(self.userop, text="Fetch Details of user by adding userid", fg="blue",font=('calibri', 30, 'bold', 'underline'))
        self.label1.grid(row=2,column=2,pady=20)
        self.label2 = Label(self.userop ,text="Enter Userid", font=('calibri', 14))
        self.label2.grid(row=3, column=1, pady=10, padx=10)
        self.ent2 = Entry(self.userop, width=50 ,textvariable=self.key  , font=('calibri', 14))
        self.ent2.grid(row=3, column=2, pady=10, padx=10)
        self.btnf = Button(self.userop, text="Fetch Details",fg="blue", font=('calibri', 14),command=self.fetch_user)
        self.btnf.grid(row=4,column=2,pady=20)
        self.label3 = Label(self.userop, text="User Name", font=('calibri', 14))
        self.label3.grid(row=5, column=1, pady=10, padx=10)
        self.ent3 = Entry(self.userop, width=50, textvariable=self.namea,font=('calibri', 14))
        self.ent3.grid(row=5, column=2, pady=10, padx=10)
        self.label4 = Label(self.userop, text="Email" ,font=('calibri', 14))
        self.label4.grid(row=6, column=1, pady=10, padx=10)
        self.ent4 = Entry(self.userop, width=50,textvariable=self.emaila, font=('calibri', 14))
        self.ent4.grid(row=6, column=2, pady=10, padx=10)
        self.label5 = Label(self.userop, text="Mobile", font=('calibri', 14))
        self.label5.grid(row=7, column=1, pady=10, padx=10)
        self.ent5 = Entry(self.userop, width=50,textvariable=self.mobilea, font=('calibri', 14))
        self.ent5.grid(row=7, column=2, pady=10, padx=10)
        self.btnu = Button(self.userop, text="Update User", fg="blue",font=('calibri', 14),command=self.update_user)
        self.btnu.grid(row=9, column=2, pady=20)
        self.btnd = Button(self.userop, text="Delete User", fg="blue", font=('calibri', 14), command=self.delete_user)
        self.btnd.grid(row=10, column=2, pady=20)
        self.btnv = Button(self.userop, text="Show All User",fg="blue", font=('calibri', 14), command=self.show_user)
        self.btnv.grid(row=11, column=2, pady=20)

        self.userop.mainloop()



    def update_user(self):
        self.id = self.ent2.get()
        self.name = self.namea.get()
        self.email = self.emaila.get()
        self.mobile = self.mobilea.get()
        #self.password = self.passworda.get()
        if self.name == "" or self.email == "" or self.mobile=="" :
            msg.showerror("ERROR", "ALL ARE REQUIRED", parent=self.userop)
        else:
                self.con = connect()
                self.cr = self.con.cursor()

                sql = f"update user set name= '{self.name}',email= '{self.email}',mobile = '{self.mobile}' where userid= '{self.id}'"
                self.cr.execute(sql)
                msg.showinfo("","User updated scuccessfully",parent=self.userop)
                self.con.commit()



    def fetch_user(self):
        self.id = self.ent2.get()
        if self.id == "":
            msg.showerror("ERROR", "FIELD ID IS REQUIRED", parent=self.userop)
        else:
                con = connect()
                cr = con.cursor()
                q = f"select userid,name ,email,mobile from user where userid='{self.id}'"
                cr.execute(q)
                var = cr.fetchone()
                if var is None:
                    msg.showerror("", "Invalid User id", parent=self.userop)
                else:
                    print(var)
                    self.namea.set(var[1])
                    self.emaila.set(var[2])
                    self.mobilea.set(var[3])
                    #self.passworda.set(var[4])
                    con.commit()
                    con.close()



    def delete_user(self):
        self.id = self.ent2.get()
        if self.id=="":
            msg.showerror("Error","Id Field is Required",parent=self.userop)
        else:
           con = connect()
           cr = con.cursor()
           cr.execute(f"DELETE from budget where userid=   '{self.id}'")
           cr.execute(f"DELETE from expense where userid=   '{self.id}'")
           cr.execute(f"DELETE from user where userid=   '{self.id}'")
           msg.showinfo("success", "user has been removed", parent=self.userop)
           con.commit()
           con.close()

    def newadmin(self):
        self.admin=Toplevel()

        self.admin.geometry("800x800")
        self.admin.title("Add admin")
        self.admin.config(bg="dodger blue")
        self.lb1 = Label(self.admin, text='Enter Name', font=('calibri', 14))
        self.lb1.grid(row=0, column=0, pady=20, padx=10)
        self.txt1 = Entry(self.admin, width=40, font=('calibri', 14))
        self.txt1.grid(row=0, column=1, pady=20, padx=10)

        self.lb2 = Label(self.admin, text='Enter Email', font=('calibri', 14))
        self.lb2.grid(row=1, column=0, pady=20, padx=10)
        self.txt2 = Entry(self.admin, width=40, font=('calibri', 14))
        self.txt2.grid(row=1, column=1, pady=20, padx=10)

        self.lb3 = Label(self.admin, text='Enter Role', font=('calibri', 14))
        self.lb3.grid(row=2, column=0, pady=20, padx=10)
        self.txt3 = ttk.Combobox(self.admin,values=['admin'], width=40, state='readonly')
        self.txt3.grid(row=2, column=1, pady=20, padx=10)

        self.lb4 = Label(self.admin, text='Enter Password', font=('calibri', 14))
        self.lb4.grid(row=3, column=0, pady=20, padx=10)
        self.txt4 = Entry(self.admin, width=40, font=('calibri', 14))
        self.txt4.grid(row=3, column=1, pady=20, padx=10)


        self.btn2 = Button(self.admin, text="SUBMIT",fg="blue", font=('calibri', 14), command=self.insertadmin)

        self.btn2.grid(row=5,column=1,pady=10)
        self.admin.mainloop()

    def insertadmin(self):
            name = self.txt1.get()
            email = self.txt2.get()
            role = self.txt3.get()
            password = self.txt4.get()

            if len(name) == 0 or len(email) == 0 or len(role) == 0 or len(password) == 0:
                msg.showwarning("", "PLease input all details....",parent=self.admin)

            else:
                con = connect()
                cur = con.cursor()
                q = f"select * from admin where email='{email}'"
                cur.execute(q)
                result = cur.fetchone()
                print(result)
                if result is None:
                    q1 = f"insert into admin values( '{name}','{email}','{password}','{role}')"
                    cur.execute(q1)
                    con.commit()
                    msg.showinfo('', "Admin added Successfully! Now Admin can Login",parent=self.root1)
                else:
                    msg.showwarning('', 'Email already exists',parent=self.admin)


    def viewadmin(self):
        self.showadmin=Toplevel()
        self.showadmin.geometry("800x800")
        self.showadmin.title("view admin")
        self.showadmin.config(bg="dodger blue")
        con = connect()
        cur = con.cursor()
        t = Text(self.showadmin, height=200, width=500)
        t.pack()
        x = pd.read_sql_query("select name,email,role from admin order by email", con)
        t.insert(tk.END, x)
        t.config(state='disabled')

    def addcat(self):
        self.adminc = Toplevel()
        # self.root.destroy()

        self.adminc.geometry("800x800")
        self.adminc.title("Add Category")
        self.adminc.config(bg="dodger blue")
        self.lb1 = Label(self.adminc, text='Enter Category', font=('calibri', 14))
        self.lb1.grid(row=0, column=0, pady=20, padx=10)
        self.txt1 = Entry(self.adminc, width=40, font=('calibri', 14))
        self.txt1.grid(row=0, column=1, pady=20, padx=10)

        self.lb2 = Label(self.adminc, text='Enter Description', font=('calibri', 14))
        self.lb2.grid(row=1, column=0, pady=20, padx=10)
        self.txt2 = Entry(self.adminc, width=40, font=('calibri', 14))
        self.txt2.grid(row=1, column=1, pady=20, padx=10)

        self.btn2 = Button(self.adminc, text="SUBMIT",fg="blue", font=('calibri', 14),
                           command=self.insertcat)

        self.btn2.grid(row=5, column=1, pady=10)
        self.admin.mainloop()



    def insertcat(self):
            category = self.txt1.get()
            description = self.txt2.get()

            if len(category) == 0 or len(description) == 0 :
                msg.showwarning("Error", "PLease input all details....",parent=self.adminc)

            else:
                con = connect()
                cur = con.cursor()
                q = f"select * from category where name='{category}'"
                cur.execute(q)
                result = cur.fetchone()
                print(result)
                if result is None:
                    q1 = f"insert into category values( '{category}','{description}')"
                    cur.execute(q1)
                    con.commit()
                    msg.showinfo('Error', "Category added Successfully!",parent=self.adminc)
                else:
                    msg.showwarning('Error', 'Category/Description already exists',parent=self.adminc)



    def viewcat(self):
        self.showview = Toplevel()
        self.showview.geometry("800x800")
        self.showview.title("view admin")
        self.showview.config(bg="dodger blue")
        con = connect()
        cur = con.cursor()
        t = Text(self.showview, height=200, width=500)
        t.pack()
        x = pd.read_sql_query("select * from category order by name", con)
        t.insert(tk.END, x)
        t.config(state='disabled')



    def show_user(self):
        self.showuser = Toplevel()
        self.showuser.geometry("800x800")
        self.showuser.title("view admin")
        con = connect()
        cur = con.cursor()
        t = Text(self.showuser, height=200, width=500)
        t.pack()
        x = pd.read_sql_query("select userid,name,email,mobile from user order by userid", con)
        t.insert(tk.END, x)
        t.config(state='disabled')

