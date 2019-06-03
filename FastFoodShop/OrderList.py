#套餐订单

from FastFoodShop.food import *
from copy import copy
class order():
    pizza=""
    snack=""
    drink=""
    def __init__(self,orderBuilder):
        self.pizza=orderBuilder.bPizza
        self.snack=orderBuilder.bSnack
        self.drink=orderBuilder.bDrink
    #多个人时再来一单
    def anotherSameOrder(self):
        return copy(self)
    def show(self):
        print("Pizza:%s"%self.pizza.getName())
        print("Snack:%s"%self.snack.getName())
        print("Drink:%s"%self.drink.getName())


class orderBuilder():
    bPizza=""
    bSnack=""
    bDrink=""
    def addPizza(self,Pizza):
        self.bPizza=Pizza
    def addSnack(self,Snack):
        self.bSnack=Snack
    def addDrink(self,Drink):
        self.bDrink=Drink

    def build(self):
        return order(self)

if  __name__=="__main__":
    pizza_factory = pizzaFactory()
    snack_factorry = snackFactory()
    drink_factory = drinkFactory()
    beef_pizza = pizza_factory.createFood(BeefPizza)
    print(beef_pizza.getName(),beef_pizza.getPrice())

    order_builder=orderBuilder()
    order_builder.addPizza(BeefPizza())
    order_builder.addSnack(fries())
    order_builder.addDrink(coke())
    order_1=order_builder.build()
    order_1.show()
    order_2=order_1.anotherSameOrder()
    order_2.show()
    dic={'order':order_1}
    print(dic['order'].pizza.getName())
