>>> a="%d %s"
>>> a%(15,"a")
'15 a'
#==============================================================================
#클래스 이름 MaxLimit
#매소드 add(숫자)
#멤버 변수에 숫자 만큼 값을 올림
#showvalue()
#멤버변수의 현재 값을 출력
# 단, 멤버 변수가 100을 넘는 순간 해당 add는 동작 하지 않음
#예시
#멤버변수가 95일때
'''
add(5)
showvalue()
===>98
'''
class MaxLimit:

    def __init__(self, val=0):#생성자
        self.val=val
        pass
    def setvalue(self,val):
        self.val=val
    def showvalue(self):
        return self.val

    def add(self,v):
        self.val +=v
        return self.val
#==============================================================================
class A:
    def __init__(self):
        self.val=40
        print("is A")

    def p(self):
        print("A")

class B(A): #extends 개념 
    def pb(self):
        self.p()
        print("B",self.__class__)
    def p(self): #메서드 오버라이딩
        print("B",self.__class__)

#===============================================================================



