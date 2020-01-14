class Calc:
    test = []
    test2 = 0
    #def __init__(self):
    #    self.val = 0
    #    pass
    def __init__(self, val=0):
        self.val = val
        pass
    def setvalue(self, val):
        self.val = val

    def showvalue(self):
        return self.val

    #인자 하나를 입력받아서, 클래스에 저장된 값과
    #입력받은 인자를 더한 값을
    #다시 클래스에 저장(업데이트) 하고
    #return 으로 돌려줌
    def add(self, v):
        self.val += v
        return self.val

    def sub(self, v):
        self.val -= v
        return self.val

    def mul(self, v):
        self.val *= v
        return self.val

    def div(self, v):
        self.val /= v
        return self.val

class Calc_5(Calc):
    def is_upper_5(self, v):
        return (v >= 100000)

    def add(self, v):
        if(self.is_upper_5(super().add(v))):
            print("5글자 이상")
            self.val = 0
            return 0
        else:
            return self.val
    
    def sub(self, v):
        if(self.is_upper_5(super().sub(v))):
            print("5글자 이상")
            self.val = 0
            return 0
        else:
            return self.val
    
    def mul(self, v):
        if(self.is_upper_5(super().mul(v))):
            print("5글자 이상")
            self.val = 0
            return 0
        else:
            return self.val
    
    def div(self, v):
        if(self.is_upper_5(super().div(v))):
            print("5글자 이상")
            self.val = 0
            return 0
        else:
            return self.val
    
    def showvalue(self):
        tmp = super().showvalue()
        print(str(tmp)[:5].zfill(5))
