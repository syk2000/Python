#클래스 이름 MaxLimit
#매소드
#add(숫자)
#   맴버 변수에 숫자 만큼씩 값을 올림
#showvalue()
#   맵버 변수의 현재 값을 출력
#단, 맴버 변수가 100을 넘는 순가,
#해당 add는 동작 하지 않음
#sub(숫자)
#   맴버 변수에 숫자 만큼씩 값을 뺌
#단, 맴버 변수가 0이하가 되지 읺도록 함
#위와 같은 방식으로

#is_hund(숫자)
#   맴버 변수가 100을 넘을지 확인
#   더했을때
#is_zero(숫자)
#   맵버 변수가 0을 넘을지 확인
#   뺐을때

#클래스 MaxLimit_up <= MaxLimit을 상속 받음
#mul(숫자)
#   맴버 변수에 숫자 만큼씩 값을 곱함
#단, 맴버 변수가 100을 넘는 순가,
#해당 mul는 동작 하지 않음

class MaxLimit:
    def __init__(self, v=0): #생성자
        self.val = v

    def __is_hund(self, v):
        return self.val + v > 100

    def is_zero(self, v):
        return self.val - v < 0
    
    def add(self, v):
        if(self.__is_hund(self,v)):
            return
        self.val += v
        
    def showvalue(self):
        return self.val
    
    def sub(self, v):
        if(self.is_zero(v)):
            return
        self.val -= v

class MaxLimit_up(MaxLimit):
    def __is_hund(self, v):
        return self.val * v > 100   
    def mul(self, v):
        if(self.__is_hund(v)):
            return
        self.val *= v









