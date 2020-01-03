goods = {"제육":4500, "짜장면":5000}


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
    ins = '-'
    while(ins != ''):
        ins = input()
        
    #구매 상품 가격 합산
    #print
    while(True):
        ins = input("구매한 상품을 등록하세요~!!!")
        if(ins== ''):
            break
        li.append(ins)

        res=0
        for i in li:
            res+=goods[i]
    print(res)
    
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
        bill():
        return True
    elif(sel == 5):
        return False
    else:
        menu()

while(menu()):
    pass

#==============================================================================
>>> li=[1,2,3,4]
>>> copy.deepcopy(li)
[1, 2, 3, 4]
>>> from copy import deepcopy
>>> deepcopy(li)

#===============================================================================
>>> import random as rd
>>> rd.random()
0.18278298049242248

>>> rd.randint(1,9)
8
>>> rd.randint(1,9)
1
>>> rd.randint(1,9)
5

>>> import random as random
>>> random.randrange(1,9,2)
5
>>> random.randrange(1,9,2)
1
>>> random.randrange(1,9,2)
1
>>> random.randrange(1,9,2)
5
>>> random.randrange(0,9,2)
0
>>> random.randrange(0,9,2)
2

>>> random.choice(["가","나","다","라"])
'나'
>>> random.choice(["가","나","다","라"])
'다'
>>> random.choice(["가","나","다","라"])
'다'
>>> random.sample(["가","나","다","라"],2)
['라', '다']

>>> import random
>>> random.random()
0.8242535590688405
>>> random()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    random()
TypeError: 'module' object is not callable

>>> from random import randint
>>> randint(1,46)
27
>>> randint(1,4)
4
>>> def randint(a,b):
	print("my func")

	
>>> randint(1,4)
my func
>>> import random
>>> random.randint(1,4)
4
>>> from random import randint
>>> randint(1,4)
3
>>> import random as rd
>>> random.randint(1,4)
1
>>> from random import randint
>>> randint(1,4)
4
>>> import random as rd
>>> random.random()
0.48645619983116395
>>> rd.random()
0.6704301903430644

#===============================================================================
#로또 게임

import random as loto

for i in range(5):
    a = loto.randint(1,45)
    print(a)

================= RESTART: D:/평일_파이썬_신윤규/day08/day08_out.py =================
24
45
14
43
38

#===============================================================================
li=[]
tmp=0
for i in range(6):
    
    while(True):
        tmp = loto.randint(1,45)
        if(tmp not in li):
            break
    li.append(tmp)
print(li)
================= RESTART: D:/평일_파이썬_신윤규/day08/day08_out.py =================
[21, 35, 37, 29, 19, 13]

#================================================================================
import random as rd


def com_

def com_rcp():
    return rd.randint(0,2)

def rcp_res(user,com):
    tmp=user-com
    if(tmp==1 or tmp==-2):
        return 1
    elif(tmp==0):
        return 0
    else:
        return -1

while(True):
    #유저는 input
    user=int(input("가위이면 0 바위이면 1 보자기이면 2를 입력해주세요~!!!"))
    #컴퓨터는 random
    com=rd.randint(0,2)
    print("유저: ",user)
    print("컴퓨터:",com)
    if(com>user):
    #유저패배
        if(user<0 or user>2):
            print("게임이 종료 되었습니다.")
            break;
        print("컴퓨터 승")
    elif(com==user):
    #동점    
        if(user<0 or user>2):
            print("게임이 종료 되었습니다.")
            break;
        print("비겼습니다.")

    elif(com<user):
        #유저 승리
        print("유저 승")
        if(user<0 or user>2):
            print("게임이 종료 되었습니다.")
            break;
        print("유저 승")

================= RESTART: D:/평일_파이썬_신윤규/day08/day08_out.py =================
가위이면 0 바위이면 1 보자기이면 2를 입력해주세요~!!!0
유저:  0
컴퓨터: 0
비겼습니다.
가위이면 0 바위이면 1 보자기이면 2를 입력해주세요~!!!1
유저:  1
컴퓨터: 1
비겼습니다.
가위이면 0 바위이면 1 보자기이면 2를 입력해주세요~!!!5
유저:  5
컴퓨터: 2
유저 승
가위이면 0 바위이면 1 보자기이면 2를 입력해주세요~!!!
================= RESTART: D:/평일_파이썬_신윤규/day08/day08_out.py =================
가위이면 0 바위이면 1 보자기이면 2를 입력해주세요~!!!5
유저:  5
컴퓨터: 1
유저 승
가위이면 0 바위이면 1 보자기이면 2를 입력해주세요~!!!
================= RESTART: D:/평일_파이썬_신윤규/day08/day08_out.py =================
가위이면 0 바위이면 1 보자기이면 2를 입력해주세요~!!!5
유저:  5
컴퓨터: 1
유저 승
가위이면 0 바위이면 1 보자기이면 2를 입력해주세요~!!!5
유저:  5
컴퓨터: 2
유저 승
가위이면 0 바위이면 1 보자기이면 2를 입력해주세요~!!!
================= RESTART: D:/평일_파이썬_신윤규/day08/day08_out.py =================
가위이면 0 바위이면 1 보자기이면 2를 입력해주세요~!!!5
유저:  5
컴퓨터: 2
유저 승
게임이 종료 되었습니다.
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day08/day08_out.py =================
가위이면 0 바위이면 1 보자기이면 2를 입력해주세요~!!!5
유저:  5
컴퓨터: 1
유저 승
게임이 종료 되었습니다.

#===============================================================================











    
