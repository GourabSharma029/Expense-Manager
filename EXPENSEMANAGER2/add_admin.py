from tkinter import *
import tkinter.messagebox as msg
from connect import connect
class add_admin:
    def __init__(self):
        self.root = Tk()
        self.root.title('ADD ADMIN')
        self.root.geometry('800x800')

        self.mainLabel = Label(self.root, text="Add New Admin", font=("calibri", 30, 'bold'))
        self.mainLabel.pack(pady=20)
        #self.loginFlag = False
        #self.signupFlag = False
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


        self.mainFrame = Frame()
        self.mainFrame.pack()

        self.btnFrame = Frame()

        self.submitBtn = Button(self.btnFrame, text="SUBMIT", font=('calibri', 14))
                               #command=self.createLogin)
        self.submitBtn.grid(row=0, column=0, padx=20)

        self.root.mainloop()
