from tkinter import *
import tkinter.messagebox as msg
from connect import connect
import userdashboard1
from PIL import Image,ImageTk

class user:
    def __init__(self):
        self.root = Tk()
        self.root.title('User Login')
        self.root.geometry('1200x1200')
        self.root.config(bg="DodgerBlue2")

        self.mainLabel = Label(self.root, text="User Login", font=("calibri", 30, 'bold'))
        self.mainLabel.pack(pady=20)
        self.loginFlag = False
        self.signupFlag = False

        self.conn = connect()
        self.cr = self.conn.cursor()

        self.mainFrame = Frame(self.root)
        self.mainFrame.pack()

        self.btnFrame = Frame(self.root,bg="DodgerBlue2")
        self.btnFrame.pack(pady=20)

        self.loginBtn = Button(self.btnFrame, text="LOGIN", font=("Impact", 15), cursor='hand2', bg="white",
                               command=self.createLogin)
        self.loginBtn.grid(row=0, column=0, padx=20)

        self.signupBtn = Button(self.btnFrame, text="REGISTER", font=("Impact", 15), cursor='hand2', bg="white",
                                command=self.createSignup)
        self.signupBtn.grid(row=0, column=1, padx=20)
        self.btnFrame.pack(pady=20)

        self.createLogin()
        self.root.mainloop()



    def createLogin(self):
        if self.loginFlag is False:
            self.loginFlag = True

            if self.signupFlag is True:
                self.signupFlag = False
                self.signupFrame.destroy()
                #self.btn2.destroy()
            #self.mainLabel.config(text="User Login",bg="blue")
            #self.loginFrame1 = Frame(self.mainFrame)
            self.frame_login = Frame(self.root, bg="white", width=500, height=400)
            self.frame_login.place(x=350, y=200)

            title = Label(self.frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="blue", bg="white").place(
                x=120, y=30)
            subtitle = Label(self.frame_login, text="User Login Area", font=("Gaudy old style", 15, "bold"), fg="black",
                             bg="white").place(x=120, y=100)
            self.lb1 = Label(self.frame_login, text="Enter Email", font=("Gaudy old style", 15, "bold"), fg="grey",
                                      bg="white").place(x=50, y=160)
            self.txt1 = Entry(self.frame_login, font=("Gaudy old style", 15), bg="white")
            self.txt1.place(x=50, y=190, width=320, height=35)
            self.lb2 = Label(self.frame_login, text="Enter Password", font=("Gaudy old style", 15, "bold"), fg="grey",
                                      bg="white").place(x=50, y=250)
            self.txt2 = Entry(self.frame_login, show='*', font=("Gaudy old style", 15), bg="white")
            self.txt2.place(x=50, y=280, width=320, height=35)
            self.btn1 = Button(self.frame_login, text="Submit", command=self.checkUser, font=("Impact", 15), fg="white",
                            cursor='hand2', bg="blue").place(x=50, y=330, width=150, height=30)



    def createSignup(self):

        if self.signupFlag is False:
            if self.loginFlag is True:
                self.loginFlag = False
                self.signupFlag = True
                self.frame_login.destroy()
                #self.btn1.destroy()

            self.signupFrame = Frame(self.root, bg="white", width=500, height=500)
            self.signupFrame.place(x=350, y=180)

            title = Label(self.signupFrame, text="Register Here", font=("Impact", 35, "bold"), fg="blue",bg="white").place(x=120, y=30)

            self.lb1 = Label(self.signupFrame, text="Enter Name", font=("Gaudy old style", 15, "bold"), fg="grey",bg="white").place(x=50, y=160)
            self.txt1 = Entry(self.signupFrame, font=("Gaudy old style", 15), bg="white")
            self.txt1.place(x=50, y=190, width=320, height=35)
            self.lb2 = Label(self.signupFrame, text="Enter Email", font=("Gaudy old style", 15, "bold"), fg="grey",
                             bg="white").place(x=50, y=220)
            self.txt2 = Entry(self.signupFrame, font=("Gaudy old style", 15), bg="white")
            self.txt2.place(x=50, y=250, width=320, height=35)
            self.lb3 = Label(self.signupFrame, text="Enter Mobile", font=("Gaudy old style", 15, "bold"), fg="grey", bg="white").place(x=50, y=290)
            self.txt3 = Entry(self.signupFrame, font=("Gaudy old style", 15), bg="white")
            self.txt3.place(x=50, y=320, width=340, height=35)
            self.lb4 = Label(self.signupFrame, text="Enter Password", font=("Gaudy old style", 15, "bold"), fg="grey",bg="white").place(x=50, y=360)
            self.txt4 = Entry(self.signupFrame, show='*', font=("Gaudy old style", 15), bg="white")
            self.txt4.place(x=50, y=390, width=320, height=35)
            self.btn2 = Button(self.signupFrame, text="Submit", command=self.insertUser, font=("Impact", 15), fg="white",cursor='hand2', bg="blue").place(x=50, y=430, width=150, height=30)
            """
            #self.mainLabel.config(text="Register new User")
            self.signupFrame = Frame(self.mainFrame)

            self.lb1 = Label(self.signupFrame, text='Enter Name', font=('calibri', 14))
            self.lb1.grid(row=0, column=0, pady=20, padx=10)
            self.txt1 = Entry(self.signupFrame, width=40, font=('calibri', 14))
            self.txt1.grid(row=0, column=1, pady=20, padx=10)

            self.lb2 = Label(self.signupFrame, text='Enter Email', font=('calibri', 14))
            self.lb2.grid(row=1, column=0, pady=20, padx=10)
            self.txt2 = Entry(self.signupFrame, width=40, font=('calibri', 14))
            self.txt2.grid(row=1, column=1, pady=20, padx=10)

            self.lb3 = Label(self.signupFrame, text='Enter Mobile', font=('calibri', 14))
            self.lb3.grid(row=2, column=0, pady=20, padx=10)
            self.txt3 = Entry(self.signupFrame, width=40, font=('calibri', 14))
            self.txt3.grid(row=2, column=1, pady=20, padx=10)

            self.lb4 = Label(self.signupFrame, text='Enter Password', font=('calibri', 14))
            self.lb4.grid(row=3, column=0, pady=20, padx=10)
            self.txt4 = Entry(self.signupFrame, width=40, font=('calibri', 14))
            self.txt4.grid(row=3, column=1, pady=20, padx=10)

            self.signupFrame.pack()
            self.btn2 = Button(self.mainFrame, text="SUBMIT", font=('calibri', 14),
                               command=self.insertUser)
            self.btn2.pack(pady=10)
            """

    def checkUser(self):
        email = self.txt1.get()
        password = self.txt2.get()
        if email=="" or password=="":
            msg.showerror("Error","All Fields are requird",parent=self.root)
        else:

            q = f"select * from user where email='{email}' and password='{password}'"
            self.cr.execute(q)
            result = self.cr.fetchone()
            if result is None:
                msg.showerror("","Invalid Email/Password",parent=self.root)
            else:
               msg.showinfo("", "Login Successful")
               self.root.destroy()
               userdashboard1.dashboard(result)


    def insertUser(self):
        name = self.txt1.get()
        email = self.txt2.get()
        mobile = self.txt3.get()
        password = self.txt4.get()

        if len(name) == 0 or len(email) == 0 or len(mobile) == 0 or len(password) == 0:
            msg.showwarning("","PLease input all details....",parent=self.mainFrame)
        else:
            q = f"select * from user where email='{email}' or mobile='{mobile}'"
            self.cr.execute(q)
            result = self.cr.fetchone()
            if result is None:
                q1 = f"insert into user values(NULL, '{name}','{email}','{mobile}','{password}')"
                self.cr.execute(q1)
                self.conn.commit()
                msg.showinfo('',"User Registered Successfully! Please Login Now",parent=self.mainFrame)
                self.createLogin()
            else:
                msg.showwarning('','Email/Mobile already exists',parent=self.mainFrame)

