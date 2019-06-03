class customer:
    customer_name=""
    snd_way=""
    info=""
    phone=""
    def setPhone(self,phone):
        self.phone=phone
    def getPhone(self):
        return self.phone
    def setInfo(self,info):
        self.info=info
    def setName(self,name):
        self.customer_name=name
    def setBrdWay(self,snd_way):
        self.snd_way=snd_way
    def sndMsg(self):
        self.snd_way.send(self.info)