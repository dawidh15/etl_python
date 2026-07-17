from eccl.Ieccl import IECCLTable

class Table(IECCLTable):
    def getPK(self):
        return super().getPK()
    
    def getType1(self):
        return super().getType1()

    def getType2(self):
        return super().getType2()
    
    def getType3(self):
        return super().getType3()