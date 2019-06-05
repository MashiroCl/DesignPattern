import sqlite3
from FastFoodShop import customer
def init_DB_user():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    '''
    考虑改成存储json数据改成存储类
    用一个函数来提取类里的信息再给views.py里使用就ok了
    '''

    c.execute('''CREATE TABLE USER
           (username nchar NOT NULL,
           password  varchar NOT NULL,
           phone   number not null);''')
    conn.commit()
    conn.close()
def init_DB_OrderList():
    '''存储数据为json'''
    conn = sqlite3.connect('orderList.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE orderList
           (orderList varchar NOT NULL,
           phone varchar NOT NULL);''')

    conn.commit()
    conn.close()

def insert_user(username1,password1,phone1):
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    sql='''insert into USER(username,password,phone) 
                VALUES (?,?,?)'''
    para=(username1,password1,phone1)
    c.execute(sql,para)
    conn.commit()
    conn.close()

def insert_orderList(data,phone):
    conn = sqlite3.connect('orderList.db')
    c = conn.cursor()
    sql='''insert into orderList(orderList,phone) 
                VALUES (?,?)'''
    para=(data,phone)
    c.execute(sql,para)
    conn.commit()
    conn.close()


def show_user():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    cursor=c.execute(''' select * from USER''')
    for row in c:
        print(row)
    conn.close()

def show_orderList():
    conn = sqlite3.connect('orderList.db')
    c = conn.cursor()
    cursor=c.execute(''' select * from orderList''')
    temp=[]
    for row in c:
        temp.append(row)
        # print(row)
    conn.close()
    return temp


if  __name__=="__main__":
    # init_DB_user()
    # insert_user('ADMIN','ADMIN','11111111111')
    # show_user("user.db")

    # init_DB_OrderList()
    # insert_orderList("MashiroCl","1111111111")

    temp=show_orderList()
    print(temp)
    print(len(temp))