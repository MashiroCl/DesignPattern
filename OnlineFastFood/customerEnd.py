from FastFoodShop import OrderList
from django.http import JsonResponse
from django.http import HttpResponse
import json
import DataBase
from django.shortcuts import render_to_response, render
import sqlite3

global temp_order

def json_to_dict(order):
    order_dict=json.loads(s=order)
    milk=order_dict["milk"]
    phone=order_dict['phone']
    beef_pizza=order_dict["beef_pizza"]
    coke=order_dict["coke"]
    fries=order_dict["chip"]
    chick_pizza=order_dict["chick_pizza"]
    chicken_wing=order_dict["chick_wing"]
    return milk,phone,beef_pizza,coke,fries,chick_pizza,chicken_wing


# 用户点击提交按钮
def commit(request):
    order=request.GET.get('data')


    temp_order=order
    milk, phone, beef_pizza, coke, fries, chick_pizza, chicken_wing=json_to_dict(order)

    order_builder=OrderList.orderBuilder()
    #加一个套餐的orderList出来  可能有加料的部分
    order_builder.addPizza(OrderList.BeefPizza())
    order_builder.addSnack(OrderList.fries())
    order_builder.addDrink(OrderList.coke())

    #判断是什么披萨
    if(beef_pizza==0):
        pass
    elif(beef_pizza==1):
        order_builder.addPizza(OrderList.BeefPizza())
    elif(beef_pizza==2):
        order_builder.addPizza(OrderList.beefDoubleDecorator(OrderList.BeefPizza()))

    if(chick_pizza==0):
        pass
    elif(chick_pizza==1):
        order_builder.addPizza(OrderList.spicyChickenPizza())

    #饮品
    if(milk==0):
        pass
    elif(milk==1):
        order_builder.addDrink(OrderList.milk())
    elif(milk==2):
        order_builder.addDrink(OrderList.chocolateDecorator(OrderList.milk()))

    if(coke==0):
        pass
    elif(coke==1):
        order_builder.addDrink(OrderList.coke())
    elif(coke==2):
        order_builder.addDrink(OrderList.iceDecorator(OrderList.coke()))

    #零食
    if(fries==0):
        pass
    elif(fries==1):
        order_builder.addSnack(OrderList.fries())

    if(chicken_wing==0):
        pass
    elif(chicken_wing==1):
        order_builder.addSnack((OrderList.chickenWings()))

    order_1=order_builder.build()
    DBorder=order_1.show()

    DataBase.insert_orderList(data=DBorder,phone=phone)


    # #再来一单
    # order_2=order_1.anotherSameOrder()
    # order_2.show()
    # dic={'order':order_1}
    # print(dic['order'].pizza.getName())

    #发到商家页面
    # return JsonResponse(dic)

    return HttpResponse("您的订单正在处理中请稍后")
