#게산기를 상속받아 기능 추가
'''
1.결과 값은 5자리를 넘을수 없음
1.1 넘을 경우 에러 출력 및 초기화

2.현재값 출력시 5자리로 출력
 ex) 5면, 00005로 출력

 3.소수 여도 역시 5자리로 총 출력
 (.포함 5글자)
'''

class Calc:
            
    def __init__(self, val=0):#생성자
        self.val=val
        pass
    def setvalue(self,val):
        self.val=val
    def showvalue(self):
        return self.val

    def add(self,v):
        #self.val +=v
        #return self.val
        def add(self,v):
        if(is_upper_5(super().add(v))):
            print("5글자 이상")
            self.val=0
            return 0
        else:
            return self.val
        

    def sub(self,v):
        #self.val -=v
        #return self.val
        def sub(self,v):
            if(self_is_upper_5(super().sub(v))):
                print("5글자 이상")
                self.val=0
                return 0
            else:
                return self.val
    
    def div(self,v):
        #self.val /=v
        #return self.val
        def div(self,v):
            if(self_is_upper_5(super().div(v))):
                print("5글자 이상")
                self.val=0
                return 0
            else:
                return self.val
    
    def mul(self,v):
        self.val *=v
        return self.val
        def mul(self,v):
            if(self_is_upper_5(super().mul(v))):
                print("5글자 이상")
                self.val=0
                return 0
            else:
                return self.val

class Calc_5(Calc):
    def is_upper_5(self,v):
        return(v>100000)

    def div(self,v):
        if(is_upper_5(super().div(v))):
            print("5글자 이상")
            self.val=0
            return 0
            
    def showvalue(self):
        tmp=super().showvalue()
        print(str(tmp).zfill(5))
        
        

    
    
