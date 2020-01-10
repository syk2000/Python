>>> path = "C:\Users\KGITBank\\Desktop\\"
>>> file=open(path+"test.txt")


>>> file=open(path+"test.txt",r)

>>> tmp=file.read()

>>> tmp

>>> def xor(n,key):
	l=[]
	for i in n:
		l.append(chr(ord(i)^key))
	return l

>>> xor(tmp,10)

>>> fil2=open(path+"dump","wb")
T
>>> a = xor(tmp,10)

>>> a

#===============================================================================

import pickle

def reg_goods(name, price):
    while(goods.get(name) != None):
        print("이미 있는 상품명 입니다.")
        name = input("다시 입력 (취소는 1) : ")
        if( name =='1'):
            return
    goods[name] =price
    

def edit_goods(name, price):
    while(goods.get(name) == None):
        print("없는 상품명 입니다.")
        tmp = input("다시 입력, 추가는 0, 취소는 1 :")
        if(tmp == '1'):
            return
        elif(tmp == '0'):
            break
        else:
            name = tmp

    goods[name] =price


            
def print_goods():
    print("============MENU============")
    for name, price in goods.items():
        print("+%-13s%12s\\+"%(name, price))
    print("============================")


def bill():
    #구매 상품 등록
    #ins = ''
    li = []
    while(True):
        ins = input("구매한 상품을 등록해 주세요")
        if(ins == ''):
            break
        elif(goods.get(ins) == None):
            print("해당 상품이 없습니다.")
            continue
        li.append(ins)
    #구매 상품 가격 합산
    #print(li)
    res = 0

    print("============BILL============")
    for i in li:
        res += goods[i]
        print("+%-13s%12s\\+"%(i, goods[i]))
    print("+%-13s%12s\\+"%("총 계",  res))
    print("============================")
    
def menu():
    print("1. 상품 추가\n2. 상품 가격 수정\n"+
          "3. 메뉴판 출력\n4. 계산서 발행\n5. 종료")
    
    sel = int(input())
    if(sel == 1):
        name = input("상품 이름을 입력해 주세요")
        price = int(input("상품 가격을 입력해 주세요"))
        reg_goods(name, price)
        return True
    elif(sel == 2):
        name = input("상품 이름을 입력해 주세요")
        price = int(input("상품 가격을 입력해 주세요"))
        edit_goods(name, price)
        return True
    elif(sel == 3):
        print_goods()
        return True
    elif(sel == 4):
        bill()
        return True
    elif(sel == 5):
        #저장
        return False
    else:
        menu()

try:
    file = open("menu.save", "rb")
    goods = pickle.load(file)
except:
    goods = {"제육":4500, "짜장면":5000}
finally:
    file.close()
    
while(menu()):
    pass

#========================================ZIP====================================
>>> min(3,5,6,8,0)
0
>>> min([3,4,5])
3
>>> zip([3,4,5],[6,7,8])
<zip object at 0x000002A554FBC408>
>>> list(zip([3,4,5],[6,7,8]))
[(3, 6), (4, 7), (5, 8)]
>>> di={1:'a',2:'b',3:'c'}
>>> di
{1: 'a', 2: 'b', 3: 'c'}
>>> for k,v in zip(di.keys(),di.values()):
	print(k,v)

	
1 a
2 b
3 c


#==============================================================================
for i,c in zip(range(len(a)),a):
	print(i,c)



>>> zip(range(len(a)),a)
>>> list(zip(range(len(a)),a))

>>> eval("112")
112
>>> eval("1+2")
3
>>> "홍길동, 나문호, 포켓몬"
'홍길동, 나문호, 포켓몬'
>>> a="홍길동, 나문호, 포켓몬"
>>> eval("li=["+a+"]")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    eval("li=["+a+"]")
  File "<string>", line 1
    li=[홍길동, 나문호, 포켓몬]
      ^
SyntaxError: invalid syntax

>>> eval("c=2")
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    eval("c=2")
  File "<string>", line 1
    c=2
     ^
SyntaxError: invalid syntax
>>> c=2
>>> eval("print(c)")
2
>>> pow(4,2)
16
>>> pow(4,-2)
0.0625

>>> import sys

>>> import time
>>> time.time
<built-in function time>
>>> time.time()
1578639294.4703047
>>> time.localtime()
time.struct_time(tm_year=2020, tm_mon=1, tm_mday=10, tm_hour=15, tm_min=55, tm_sec=3, tm_wday=4, tm_yday=10, tm_isdst=0)
>>> time.localtime(0)
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=9, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

>>> time.asctime()
'Fri Jan 10 15:59:11 2020'
>>> time.asctime(time.localtime(0))
'Thu Jan  1 09:00:00 1970'

>>> for i in range(10):
	print(i)
	time.sleep(2)

	
0
1
2
3
4
5
6
7
8
9
>>> time.sleep(1);print("hi")
hi

>>> result=0
>>> def add(num):
	global result
	result += num
	return result

>>> add(3)
3
>>> add(4)
7
>>> add(2)
9
>>> result2=0
>>> def add2(num):
	global result
	result+=num
	return result

>>> add2(4)
13
>>> class Calc:
	def __init__(self):
		self.reesult=0
	def add(self, num):
		self.result += num
		return self.result

	
>>> call = Calc()

>>> class test:
	pass

>>> a=test()
>>> type(a)
class '__main__.test'>


>>> t = Calc()
>>> type(t)
<class '__main__.Calc'>

#==============================================================================
class Calc:
    def setvalue(self,v):
        self.val=v

    def showvalue(self):
================= RESTART: D:/평일_파이썬_신윤규/day13/day13_out.py =================
>>> cal =Calc()
>>> type(cal)
<class '__main__.Calc'>
>>> cal.setvalue(30)
>>> cal.showvalue()
30

>>> cal2 = Calc()       #object
>>> cal2.showvalues()

#===============================================================================
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
        self.val += v

        return self.val
#===============================================================================
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






