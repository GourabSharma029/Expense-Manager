import pymysql
def connect():
    con=pymysql.connect(host="127.0.0.1",
                        user='root',
                        password='',
                        database='expensemanagero')
    return con