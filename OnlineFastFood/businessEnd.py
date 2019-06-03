from FastFoodShop import  OrderList
from FastFoodShop import  infoSystem
from FastFoodShop import  acceptOrder

def inform_kitchen(request):
    request.GET.get('order')
    #通知后厨的部分就在后台输出当作通知
    print("")

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
