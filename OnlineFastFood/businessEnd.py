from FastFoodShop import  OrderList
from FastFoodShop import  infoSystem
from FastFoodShop import  acceptOrder
from OnlineFastFood import customerEnd
import json

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


def inform_kitchen(request):
    #通知后厨的部分就在后台输出当作通知
    
    order=customerEnd.temp_order
    milk, phone, beef_pizza, coke, fries, chick_pizza, chicken_wing = json_to_dict(order)


    pizza_factory = OrderList.pizzaFactory()
    snack_factory = OrderList.snackFactory()
    drink_factory = OrderList.drinkFactory()


    pizza=""
    snack=""
    drink=""


    #判断是什么披萨
    if(beef_pizza==0):
        pass
    elif(beef_pizza==1):
        pizza=pizza_factory.createFood(OrderList.BeefPizza)
    elif(beef_pizza==2):
        pizza=pizza_factory.createFood(OrderList.BeefPizza)
        pizza=OrderList.beefDoubleDecorator(pizza)

    if(chick_pizza==0):
        pass
    elif(chick_pizza==1):
        pizza = pizza_factory.createFood(OrderList.spicyChickenPizza)

    #饮品
    if(milk==0):
        pass
    elif(milk==1):
        drink=drink_factory.createFood(OrderList.milk)
    elif(milk==2):
        drink = drink_factory.createFood(OrderList.milk)
        drink = OrderList.chocolateDecorator(drink)

    if(coke==0):
        pass
    elif(coke==1):
        drink = drink_factory.createFood(OrderList.coke)
    elif(coke==2):
        drink = drink_factory.createFood(OrderList.coke)
        drink = OrderList.iceDecorator(drink)


    #零食
    if(fries==0):
        pass
    elif(fries==1):
        snack=snack_factory.createFood(OrderList.fries)

    if(chicken_wing==0):
        pass
    elif(chicken_wing==1):
         snack=snack_factory.createFood(OrderList.chickenWings)


    print(pizza)
    print(snack)
    print(drink)

def inform_customer(request):
    #获得用户的电话号码
    order = request.GET.get('data')
    milk, phone, beef_pizza, coke, fries, chick_pizza, chicken_wing = json_to_dict(order)

    customer_x=infoSystem.customer.customer()
    customer_x.setName("CUSTOMER")
    customer_x.setPhone(phone=phone)

    #信息通知用户
    customer_x.setInfo("Welcome to our new party!")
    text_sender=infoSystem.textSender()
    customer_x.setBrdWay(text_sender)
    customer_x.sndMsg()

    #电话通知用户
    text_phone_caller=infoSystem.phoneCaller()
    customer_x.setBrdWay(text_phone_caller)
    customer_x.sndMsg()


def inform_takefood(request):
    order = request.GET.get('data')
    phone=order['phone']
    temp_phone=phone[-4:]
    ready_to_deliver=acceptOrder.ReadyToDeliver()
    ready_to_deliver.runAll(1,2,"尾号为"+temp_phone+" 请取餐")



'''
        前端不停刷新页面
        用户commit的数据由customerEnd.py内的Commit函数发往商家页面
        一旦有了数据就会显示
'''