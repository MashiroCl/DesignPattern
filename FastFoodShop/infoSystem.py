from FastFoodShop import customer
class msgSender:
    def send(self,info):
        pass
class phoneCaller(msgSender):
    def send(self,info):
        print("phone is ringing %s"%(info))
class textSender(msgSender):
    def send(self,info):
        print("text send to%s"%(info))


if  __name__=="__main__":
    customer_x=customer.customer()
    customer_x.setName("CUSTOMER_X")
    customer_x.setPhone("10023456789")

    customer_x.setInfo("Welcome to our new party!")

    text_sender=textSender()
    customer_x.setBrdWay(text_sender)
    customer_x.sndMsg()

    text_phone_caller=phoneCaller()
    customer_x.setBrdWay(text_phone_caller)
    customer_x.sndMsg()