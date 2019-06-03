from django.http import HttpResponse
from django.forms import forms
from django.shortcuts import render
from django.http import JsonResponse
import sqlite3
from django.http import HttpResponse
# Create your views here.
DB_path="E:/Pycharm/workspace/style_change_web/user.db"


def register(request):
    return HttpResponse('register.html')

def registerCheck(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    conn = sqlite3.connect('user.db')
    c=conn.cursor()
    cursor = c.execute("select * from user where username='%s'" % (username))
    # 用户名已被注册
    if (len(list(cursor)) != 0):
         return HttpResponse('')                #注册界面显示用户名已经被注册
    else:
        c.execute("insert into USER(username,password) VALUES ('%s','%s')"%(username,password))
        conn.commit()
    conn.close()
    return HttpResponse('sign.html')

def sign(request):
    return HttpResponse('sign.html')

def signCheck(request):
    username=request.POST.get('')   #label needed
    password = request.POST.get('')  # label needed
    db=sqlite3.connect(DB_path)
    c=db.cursor()


    cursor = c.execute("select * from user where username='%s'" % (username))
    db.close()

    # 用户未注册
    if (len(list(cursor)) == 0):
         return HttpResponse()      #缺一个登录需要注册界面


    #用户名与密码不匹配
    for row in cursor:
        _username=row[0]
        _password=row[1]
    if (_password != password):
        return HttpResponse()     #缺一个密码输入错误界面

    # 是商家
    if(username=="ADMIN" and password=="ADMIN"):
        return HttpResponse("admin.html")
    '''
        商家界面能进行的操作：
        1.有单子的时候可以确认接单 接单后会以行的形式显示，行的右端有按钮：通知后厨 进行派送
        2.通知后厨 用food.py里的factory进行食物制作
        3.执行acceptOrder.py里的ReadyToDeliver来进行外卖派送
    '''


    #普通用户成功登录
    return HttpResponse("customer.html")
'''
        用户界面能进行的操作：
        1.选择pizza,snack,drink用OrderList.py里的add函数来组成一个套餐
        2.选完套餐可以提交，提交之后会出现按钮：再来一单
'''

def index(request):
    return HttpResponse('牵牛花与加濑同学')

def home(request):
    return HttpResponse('customer.html')


