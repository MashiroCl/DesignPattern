import sqlite3
from FastFoodShop import customer
def init_DB():
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

def test_insert():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('''insert into USER(username,password,phone) 
                VALUES ('ADMIN','ADMIN','11111111111')''')
    conn.commit()
    conn.close()

def show():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    cursor=c.execute(''' select * from USER''')
    for row in c:
        print(row)
    conn.close()

init_DB()
# test_insert()
show()