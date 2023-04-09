import datetime
from tkinter import *
import tkinter.ttk as ttk
from connect import connect
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class main:
    def __init__(self, userid):
        self.root = Tk()
        self.root.title("Graph view")
        self.root.geometry('800x800')
        self.root.config(bg="SteelBlue1")
        self.userid = userid
        self.mainLabel = Label(self.root, text="View Expense Graphs", font=('calibri', 30, 'bold', 'underline'))
        self.mainLabel.pack(pady=20)

        self.comb = ttk.Combobox(self.root, values=("Monthly Expenses",),
                                 state='readonly', font=('arial', 12))
        self.comb.pack(pady=10)
        self.comb.set('Monthly Expenses')
        self.comb.bind("<<ComboboxSelected>>", self.plotChart)

        self.frame = Frame(self.root)


        self.frame.pack()
        self.plotMonthlyChart()

        self.root.mainloop()

    def plotChart(self, event):
        self.choice = self.comb.get()
        if self.choice == 'Monthly Expenses':
            self.plotMonthlyChart()
        else:
            pass

    def plotMonthlyChart(self):
        month = str(datetime.datetime.now().month)
        year = datetime.datetime.now().year
        month = str(month)
        if len(month) == 1:
            month = f"0{month}"
        self.conn = connect()
        self.cr = self.conn.cursor()
        q1 = f"select date,amount, category from expense where userid='{self.userid}'"
        self.cr.execute(q1)
        alldata = self.cr.fetchall()

        print(alldata)
        self.categories = {}
        for i in alldata:
            if str(i[0])[0:7] == f"{year}-{month}":
                if i[2] in self.categories:
                    self.categories[i[2]] += i[1]
                else:
                    self.categories[i[2]] = i[1]

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.pie(x=list(self.categories.values()), labels=list(self.categories.keys()))

        canvas = FigureCanvasTkAgg(figure=f, master=self.frame)
        canvas.get_tk_widget().pack()

    def plotGraph(self):
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,34,5],[3,4,5,6])

        canvas = FigureCanvasTkAgg(figure=f, master=self.frame)
        canvas.get_tk_widget().pack()



