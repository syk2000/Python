
class Calc:
    
    def __init__(self):
        self.val=0
        pass
    def setvalue(self,val):
        self.val=val

    def showvalue(self):
        return self.val
        

    #인자 하난르 입력받아 클래스에 저장된 값과
    #입력받은 인자를 더한 값을
    #다시 클래스에 저장(업데이트)하고
    #return으로 돌려줘라

    def add(self,val):
        self.val += val

        return self.val

    def mul(self,val):
        self.val *=  val

        return self.val
    def sub(self,val):
        self.val -=  val

        return self.val
    def div(self,val):
        self.val //  val

        return self.val
         
