#商家选择骑手送外卖的时候
class informDeliver:
    def select(self,num):
        #通知骑手
        print("no. %s Deliver has been selected"%(num))
#通知餐厅前台准备好，骑手去几号窗口取餐
class informWaiter:
    def ready(self,num):
        print("%s 前台准备接待骑手"%(num))
#打印小票
class receipt:
    def print(self,info):
        print("printing %s"%(info))

class ReadyToDeliver:
    def __init__(self):
        self.info_deliver=informDeliver()
        self.info_waiter=informWaiter()
        self.receipt=receipt()
    def runAll(self,num1,num2,info):
        self.info_deliver.select(num1)
        self.info_waiter.ready(num2)
        self.receipt.print(info)

if __name__=="__main__":
    ready_to_deliver=ReadyToDeliver()
    ready_to_deliver.runAll(1,2,"jojo")

