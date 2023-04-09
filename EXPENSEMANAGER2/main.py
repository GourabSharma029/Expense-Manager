from tkinter import *
import ADMINLOGIN
import userloginsignup

class first:
    def __init__(self):
        self.one=Tk()
        self.one.title('Expense Manager')
        self.one.state('zoomed')
        self.one.config(bg="blue")

        self.bg = PhotoImage(file=r"C:\Users\GOURAB SHARMA\Downloads\WhatsApp Image 2022-10-01 at 11.47.28 (1).png")
        self.bg_image = Label(self.one, bg="white", image=self.bg).place(x=400, y=250)

        self.mainLabel = Label(self.one, text="WELCOME HERE", font=("calibri", 30, 'bold'))
        self.mainLabel.pack()
        self.mainLabel1 = Label(self.one, text="EXPENSE MANAGER KEEP RECORD OF UR EXPENSES",fg="blue", font=("calibri", 30, 'bold'))
        self.mainLabel1.pack(pady=20)

        self.mainlabel2=Label(self.one,text="SELECT UR ROLE:", font=("calibri", 30, 'bold'))
        self.mainlabel2.pack(pady=20)

        frame_login = Frame(self.one, bg="white")
        frame_login.pack(pady=50,padx=20)

        self.adminloginm = Button(frame_login, text="ADMIN", font=('calibri', 20),fg="blue",width=10, command=self.adminlogin)
        self.adminloginm.grid(row=0, column=1,padx=150)

        self.userloginm = Button(frame_login, text="USER", font=('calibri', 20),fg="blue",width=10, command=self.userlogin)
        self.userloginm.grid(row=0, column=0,padx=20)

        self.one.mainloop()
    def adminlogin(self):
        ADMINLOGIN.main()




    def userlogin(self):
        userloginsignup.user()
    


first()