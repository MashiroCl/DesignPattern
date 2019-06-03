from FastFoodShop import OrderList
from django.http import JsonResponse
# 用户点击提交按钮
def commit(request):
    pizza_factory = OrderList.pizzaFactory()
    snack_factorry = OrderList.snackFactory()
    drink_factory = OrderList.drinkFactory()
    #判断是什么披萨
    beef_pizza = pizza_factory.createFood(OrderList.BeefPizza)
    chicken_pizza=pizza_factory.createFood(OrderList.spicyChickenPizza)
    print(beef_pizza.getName(),beef_pizza.getPrice())

    order_builder=OrderList.orderBuilder()

    #加一个套餐的orderList出来  可能有加料的部分
    order_builder.addPizza(OrderList.BeefPizza())
    order_builder.addSnack(OrderList.fries())
    order_builder.addDrink(OrderList.coke())

    order_1=order_builder.build()
    order_1.show()
    order_2=order_1.anotherSameOrder()
    order_2.show()
    dic={'order':order_1}
    print(dic['order'].pizza.getName())
    return JsonResponse(dic)