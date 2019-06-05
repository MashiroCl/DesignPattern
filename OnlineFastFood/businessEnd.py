from FastFoodShop import  OrderList
from FastFoodShop import  infoSystem
from FastFoodShop import  acceptOrder
import json

def inform_kitchen(request):
    #通知后厨的部分就在后台输出当作通知
    order=request.GET.get('data')
    order_dict=json.loads(s=order)
    milk=order_dict["milk"]

    print(milk)
    beef_pizza=order_dict["beef_pizza"]
    coke=order_dict["coke"]
    fries=order_dict["chip"]
    chick_pizza=order_dict["chick_pizza"]
    chicken_wing=order_dict["chick_wing"]
    #
    # #获得用户的信息
    # # # phone=request.GET.get('')


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
    #获得用户的用户名，电话号码
    username=request.GET.get('')

    customer_x=infoSystem.customer.customer()
    customer_x.setName("CUSTOMER_X")
    customer_x.setPhone("10023456789")

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
    ready_to_deliver=acceptOrder.ReadyToDeliver()
    ready_to_deliver.runAll(1,2,"jojo")



'''
        前端不停刷新页面
        用户commit的数据由customerEnd.py内的Commit函数发往商家页面
        一旦有了数据就会显示
'''