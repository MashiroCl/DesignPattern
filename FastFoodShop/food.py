#通知后厨及进行生产
#PIZZA
class Pizza():
    name=""
    price=0.0
    type="Pizza"
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def getName(self):
        return self.name
class BeefPizza(Pizza):
    def __init__(self):
        self.name="beef pizza"
        self.price=80.0
class spicyChickenPizza(Pizza):
    def __init__(self):
        self.name="spicy chicken pizza"
        self.price=60.0

#SNACK
class Snack():
    name=""
    price=0.0
    type="Snack"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name
class fries(Snack):
    def __init__(self):
        self.name="fries"
        self.price=10.0
class chickenWings(Snack):
    def __init__(self):
        self.name="fries"
        self.price=10.0

class Drink():
    name = ""
    price = 0.0
    type="Drink"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name
class coke(Drink):
    def __init__(self):
        self.name = "coke"
        self.price = 3.0
class milk(Drink):
    def __init__(self):
        self.name = "milk"
        self.price = 4.0

#通知后厨进行食物制作
class foodFactory():
    def createFood(self,foodClass):
        print(self.type,"is producing")
        food=foodClass()
        return food
class pizzaFactory(foodFactory):
    def __init__(self):
        self.type="Pizza"
class snackFactory(foodFactory):
    def __init__(self):
        self.type="Snack"
class drinkFactory(foodFactory):
    def __init__(self):
        self.type="Drink"


#饮料加料
class drinkDecorator():
    def getName(self):
        pass

    def getPrice(self):
        pass


class iceDecorator(drinkDecorator):
    def __init__(self, drink):
        self.drink = drink

    def getName(self):
        return self.drink.getName() + " +ice"

    def getPrice(self):
        return self.drink.getPrice() + 1.0


class chocolateDecorator(drinkDecorator):
    def __init__(self, drink):
        self.drink = drink

    def getName(self):
        return self.drink.getName() + " +chocolate"

    def getPrice(self):
        return self.drink.getPrice() + 3.0


#Pizza加料
class pizzaDecorator():
    def getName(self):
        pass
    def getPrice(self):
        pass
class beefDoubleDecorator(pizzaDecorator):
    def __init__(self, drink):
        self.drink = drink

    def getName(self):
        return self.drink.getName() + " +doubleBeef"

    def getPrice(self):
        return self.drink.getPrice() + 20.0



#先生成factory,再生成一个实例，输出一句话加价格
if  __name__=="__main__":
    pizza_factory=pizzaFactory()
    snack_factorry=snackFactory()
    drink_factory=drinkFactory()
    beefPizza=pizza_factory.createFood(BeefPizza)
    print(beefPizza.getName(),beefPizza.getPrice())
    # chicken_wings=snack_factorry.createFood(chickenWings)
    # print chicken_wings.getName(),chicken_wings.getPrice()
    coke_drink=drink_factory.createFood(coke)
    print(coke_drink.getName(),coke_drink.getPrice())


    ice_coke=iceDecorator(coke_drink)
    print(ice_coke.getName())
    double_beef_pizza=beefDoubleDecorator(beefPizza)
    print(double_beef_pizza.getName())
