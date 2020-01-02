>>> a=(1,[2,3],4)
>>> a[1]
[2, 3]
>>> a[1].append(3)
>>> a
(1, [2, 3, 3], 4)
>>> a,b=3,4
>>> a,b=b,a
>>> a
4
>>> b
3
def test():
	print("hello world")

	
>>> test()
hello world
>>> test()
hello world
>>> def test(n):
	for i in range(n):
		print("hellow world")

		
>>> test(4)
hellow world
hellow world
hellow world
hellow world

>>> def test(n=1):
	for i in range(n):
		print("hellow world")

		
>>> test()
hellow world
>>> test(a=123)
{'a': 123}

>>> def sum_many(*v):
	res = 0
	for i in v:
		res+=i
	return res

>>> def avg_many(*v):
	return (sum_many(*v) / len(v))

>>> sum_many(3,3,3)
9
>>> avg_many(3,3,3,3)
3.0
>>> def ttttt(*v, **k):
	print(type(V))
	print(type(k))

>>> di={1:"a",2:"c"}
>>> di[1]
'a'
>>> di[2]
'c'
>>> stu={"이름":"홍길동","학과":"컴퓨터","학번":"123415"}
>>> stu["이름"]
'홍길동'
>>> stu
{'이름': '홍길동', '학과': '컴퓨터', '학번': '123415'}

>>> for i in stu:
	print(i)

	
이름
학과
학번

stu.keys()
dict_keys(['이름', '학과', '학번'])

>>> stu.values()
dict_values(['홍길동', '컴퓨터', '123415'])

>>> di
{1: 'a', 2: 'c'}

>>> a="d"
>>> di[a]=4
>>> di
{1: 'a', 2: 'c', 'd': 4}
>>> print(di)
{1: 'a', 2: 'c', 'd': 4}

#==============================================================================
c= input()
a=input()

ex={"이름":c,"전공":a}

================= RESTART: D:/평일_파이썬_신윤규/day07/day07_out.py =================
홍길
안녕
>>> ex["이름"]
'홍길'
>>> ex.keys()
dict_keys(['이름', '전공'])
>>> ex.values()
dict_values(['홍길', '안녕'])
>>> ex.clear()
>>> ex
{}

#===============================================================================
>>> di={}
>>> di[7]=9
>>> di
{7: 9}
>>> di.get(7)=10
SyntaxError: can't assign to function call
>>> di.clear()
>>> di
{}

>>> import collections
>>> di2 = collections.OrderedDict()
>>> di
{}
>>> di.get(4)
>>> di.setdefault(4,0)
0

>>> di[1]=3
>>> di
{4: 0, 1: 3}
>>> di.setdefault(5,0)
0
>>> di
{4: 0, 1: 3, 5: 0}

>>> stu={"이름":"홍길동"}
>>> stu
{'이름': '홍길동'}
>>> di.update(stu)
>>> di
{4: 0, 1: 3, 5: 0, '이름': '홍길동'}

>>> di.pop(4)
0

>>> di
{1: 3, 5: 0, '이름': '홍길동'}


>>> key=(1,2,3,4)
>>> di.clear
<built-in method clear of dict object at 0x000001BAE53AE2D0>
>>> di.clear()
>>> di
{}
>>> di.fromkeys(key)
{1: None, 2: None, 3: None, 4: None}
>>> di
{}
>>> di.update(stu)
>>> di
{'이름': '홍길동'}
>>> di.fromkeys(key)
{1: None, 2: None, 3: None, 4: None}
>>> di.fromkeys(('지역','학과'))
{'지역': None, '학과': None}
>>> dict.fromkeys((1,2,3))
{1: None, 2: None, 3: None}
>>> dict.fromkeys((1,2,3))
{1: None, 2: None, 3: None}
>>> dict.fromkeys((1,2,3),('a','b','c'))
{1: ('a', 'b', 'c'), 2: ('a', 'b', 'c'), 3: ('a', 'b', 'c')}

>>> num={1:"일",2:"이",3:"삼",4:"사"}
>>> num[1]
'일'
>>> num.keys()
dict_keys([1, 2, 3, 4])
>>> num.values()
dict_values(['일', '이', '삼', '사']) #list로 형변환
>>> list(num.keys())
[1, 2, 3, 4]

#===============================================================================
#가수 이름, 구성원, 대표곡을 input으로 입력
#for 문을 사용하되, values()를 사용하지 않고
#이름, 구성원, 대표곡의 value만을 각각 출력
# 구성운 key에 value로 구성원 수만 입력

singer={}

for i in range(3):
    if(i==0):
        singer['가수 이름']= input()
        singer
        
    elif(i==1):
        singer['구성원']= input()
        singer
        
    else:
        singer['대표곡']= input()
        singer

================= RESTART: D:/평일_파이썬_신윤규/day07/day07_out.py =================
아이유
01
좋은날
>>> singer
{'가수 이름': '아이유', '구성원': '01', '대표곡': '좋은날'}

#===============================================================================
#앞으로 수정이 필요한 것
#
menu={}

for i in range(3):
    if(i%3==0):
        menu['음식 번호']= int(input())
        
    elif(i%3==1):
        menu['음식 이름']= input()
        
    elif(i%3==2)
        menu['가격']= input()

a=menu['음식 번호']
b=menu['음식이름']
c=menu['가격']

dict.fromkeys(())

#================================================================================
>>> goods={'연필':500,"자":1000}
>>> name = '색연필'
>>> price = 1000
>>> goods[name] = price


#메뉴 생성
goods={}
def reg_goods(name,price):
    while(goods.get(name) !=None):
        print("이미 있는 상품명 입니다.")
        name = input("다시 입력 (취소는 1)")
        if(name == '1'):
            return
    goods[name] = price



#메뉴 수정
def edit_goods(name,price):
    while(goods.get(name) == None):
        print("없는 작품명 이빈다.")
        tmp = input("다시 입력. 추가는 0,취소는 1 :")
        if(tmp=='1'):
            return
        elif(tmp=='0'):
            break
        else:
            name = tmp

    goods[name]=  price

    '''
def del_goods(name,price):
    while(goods.get(name) != None):
        print("삭제 하시겠습니까?")
        out = input("Yes: 1 ,No: 2")
        if(out==1):

            print("삭제 처리가 되었습니다.")
        else:
            return

    goods[name]=price
'''
#예쁘게 출력하게 만들기  
def print_goods():
    print("===========================Menu==============================")
    for name, price in goods.items():
        print("+%-13s%13s+"%(name,price))
        print("===============================================================")


def menu():
    print("1. 상품추가 \n2. 상품 가격 수정\n3. 메뉴판 출력\n4. 계산서 발행\n5. 종료")

    sel = int(input())
    if(sel==1):
        name = input("상품 이름을 입력해 주세요")
        price = input("상품 가격을 입력해 주세요")
        reg_goods(name,price)
        return True
    elif(sel ==2):
        name = input("상품 이름을 입력해 주세요")
        price = input("상품 가격을 입력해 주세요")
        reg_goods(name,price)
        return True
    elif(sel==3):
        print_goods()
        return True
    elif(sell==4):
        return True
    elif(sel==5):
        return False
    else:

================= RESTART: D:/평일_파이썬_신윤규/day07/day07_out.py =================
>>> edit_goods("짬뽕",5500)
없는 작품명 이빈다.
다시 입력. 추가는 0,취소는 1 :0
>>> goods
{'짬뽕': 5500}
>>> reg_goods("제육",4500)
>>> goods
{'짬뽕': 5500, '제육': 4500}
>>> edit_goods("짬짜면",5500)
없는 작품명 이빈다.
다시 입력. 추가는 0,취소는 1 :0
>>> goods
{'짬뽕': 5500, '제육': 4500, '짬짜면': 5500}

#===============================================================================










