from tkinter import *
import tkinter.messagebox as msg
from connect import connect
import userloginsignup
import admindashboard
class change:
    def __init__(self):
        self.change=Tk()
        self.change.geometry("1200x1200")
        self.change.title("CHANGE PASSWORD")
        self.change.config(bg="SkyBlue3")
        self.titlechangea = Label(self.change, text="CHANGE UR PASSWORD",fg="blue", font=("calibri", 20, 'bold'))
        self.titlechangea.grid(row=3, column=1,pady=20)
        self.titlechange =Label(self.change,text="ENTER OLD PASSWORD", font=("calibri", 20, 'bold'))
        self.titlechange.grid(row=4,column=0,pady=20)
        self.titlechangee =Entry(self.change, font=("calibri", 20, 'bold'))
        self.titlechangee.grid(row=4,column=1,pady=20)
        self.titlechange1 = Label(self.change, text="ENTER NEW PASSWORD", font=("calibri", 20, 'bold'))
        self.titlechange1.grid(row=5, column=0,pady=20)
        self.titlechangee1 = Entry(self.change, font=("calibri", 20, 'bold'))
        self.titlechangee1.grid(row=5, column=1,pady=20)
        self.titlechange2 = Label(self.change, text="REENTER NEW PASSWORD", font=("calibri", 20, 'bold'))
        self.titlechange2.grid(row=6, column=0,pady=20)
        self.titlechangee2 = Entry(self.change, font=("calibri", 20, 'bold'))
        self.titlechangee2.grid(row=6, column=1,pady=20)
        self.mail = Label(self.change, text="Enter Email", font=("calibri", 20, 'bold'))
        self.mail.grid(row=7, column=0, pady=20)
        self.maile = Entry(self.change, font=("calibri", 20, 'bold'))
        self.maile.grid(row=7, column=1, pady=20)

        changebtn=Button(self.change,text="CHANGE",bg="blue", font=("calibri", 20, 'bold'),command=self.changep)
        changebtn.grid(row=8,column=1,pady=20)
        #self.password=userloginsignup.self.txt2
        self.change.mainloop()

    def changep(self):
            self.old=self.titlechangee.get()
            self.new=self.titlechangee1.get()
            self.renter=self.titlechangee2.get()
            self.email=self.maile.get()
            if self.old=="" or self.new=="" or self.renter=="" or self.email=="":
                msg.showwarning("","all fields are required",parent=self.change)
            #if self.old == self.new:
            #    msg.showwarning("","new and old password cannot be same",parent=self.change)
            if self.new!=self.renter:
                msg.showwarning("","new and reenter new password must be same",parent=self.change)
            else:

                con = connect()
                cur = con.cursor()
                q = f"select * from admin where  email='{self.email}' and password='{self.old}' "
                cur.execute(q)
                result = cur.fetchone()
                print(result)


                if result is not None:

                    q = f"update admin set password='{self.new}' where email='{self.email}'"
                    cur.execute(q)
                    result1 = cur.fetchone()
                    print(result1)

                    con.commit()
                    # self.admin.destroy
                    msg.showinfo('', "Password updated Successfully! Now Admin can Login with new password", parent=self.change)
                else:
                    msg.showwarning("","WRONG details",parent=self.change)

