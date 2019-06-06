import json
from django.shortcuts import render_to_response, render
import sqlite3
from django.http import HttpResponse
import DataBase
from django.shortcuts import redirect  #重新定向模块

DB_path="E:/Pycharm/workspace/style_change_web/user.db"


def register(request):
    return render_to_response('register.html')

def registerCheck(request):
    data=request.GET.get("data")
    sdata=json.loads(s=data)
    username=sdata["username"]
    password=sdata["password"]
    phone=sdata["phone"]

    print(username)
    print(password)
    print(phone)

    conn = sqlite3.connect('user.db')
    DataBase.insert_user(username,password,phone)
    return redirect('http://127.0.0.1:8000/sign.html')

def sign(request):
    return render_to_response('sign.html')

def signCheck(request):
    data=request.GET.get("data")
    sdata=json.loads(s=data)
    username=sdata["username"]
    password=sdata["password"]
    print(username)
    print(password)
    # db=sqlite3.connect(DB_path)
    # c=db.cursor()
    #
    #
    # cursor = c.execute("select * from user where username='%s'" % (username))
    # db.close()

    # # 用户未注册
    # if (len(list(cursor)) == 0):
    #      return HttpResponse()      #缺一个登录需要注册界面


    # #用户名与密码不匹配
    # for row in cursor:
    #     _username=row[0]
    #     _password=row[1]
    # if (_password != password):
    #     return HttpResponse()     #缺一个密码输入错误界面

    # 是商家
    if(username=="ADMIN" and password=="ADMIN"):
       admin_data()
    '''
        商家界面能进行的操作：
        1.有单子的时候可以确认接单 接单后会以行的形式显示，行的右端有按钮：通知后厨 进行派送
        2.通知后厨 用food.py里的factory进行食物制作
        3.执行acceptOrder.py里的ReadyToDeliver来进行外卖派送
    '''

    print("lalaallalala")
    #普通用户成功登录
    return redirect("https://www.baidu.com")
'''
        用户界面能进行的操作：
        1.选择pizza,snack,drink用OrderList.py里的add函数来组成一个套餐
        2.选完套餐可以提交，提交之后会出现按钮：再来一单
'''

def index(request):
    print("Here is index")
    return HttpResponse('牵牛花与加濑同学')


def customerPage(request):
    return render_to_response('user.html')

def admin_data(request):
    temp=DataBase.show_orderList()
    order_num=len(temp)
    dict={}
    for i in range(order_num):
        dict[temp[i][1]]=temp[i][0]
    dict=json.dumps(dict)
    print("admin_data ",dict)
    return render(request, 'host.html', {'data': dict})



