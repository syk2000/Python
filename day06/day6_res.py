a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
>>> a
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> a[0]
[1, 2, 3]
>>> a[0][0]
1


#===============================================================================
>>> for i in range(3):
	for j in range(3):
		a[i][j]
		print(a)

		
1
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
2
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
3
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
4
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
5
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
6
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
7
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
8
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
9
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#===============================================================================

>>> for i in range(3):
	for j in range(3):
		print(a[i][j])

		
1
2
3
4
5
6
7
8
9

>>> c=[1,2,3,4,5,6,7,8,9]
>>> c[4]
5
>>> c[-3]
7
#파이썬은 음수기호도 추가가 되었다.
>>> c[2:-5]
[3, 4]
>>> c[-7:8]
[3, 4, 5, 6, 7, 8]


#===============================================================================
ls=[
    [["이름"],["나이"],["주소"],["지울값"],["연봉"]],
    [["홍길동"],["20살"],["산골지기"],["지우세요"],["5000"]],
    [["김개똥"],["30살"],["지구촌"],["지우세요"],["4500"]]
    ]

for i in range(len(ls)):
    del(ls[i][3])#지울 값 삭제
    if(i != 0):#첫번째 줄은 글자 이므로 다음 줄부터 적용
        ls[i][-1][0] = str(int(int(ls[i][-1][0])*1.1))
        #문자가 들어있는 "배열"임으로
        #[-1]로 마지막 것을 선택 후 다시 [0]으로 항목
        #int(...)*1.1은 실수가 되므로 다시 int를 써서 정수로 바꿈
        #그러지 않으면 5500.000과 같이 출력된다.
    for j in range(len(ls[i])):
        print(ls[i][j],end="")
    print("")

=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
['이름']['나이']['주소']['연봉']
['홍길동']['20살']['산골지기']['5500']
['김개똥']['30살']['지구촌']['4950']


#===============================================================================
# 튜플

>>> a=(1,2,3)
>>> print(a)
(1, 2, 3)
>>> b=[1,2,3]
>>> print(a)
(1, 2, 3)
>>> print(b)
[1, 2, 3]
>>> print(b[0])
1
>>> b[:1]
[1]
>>> len(b)
3
>>> len(a)
3
>>> a[:1]
(1,)
>>> a[:2]
(1, 2)
>>> type(a)
<class 'tuple'>
>>> b[1]
2
>>> b[1] = 3
>>> b
[1, 3, 3]

>>> 1,2,3
(1, 2, 3)
>>> a=1,2,3,4
>>> a
(1, 2, 3, 4)
>>> type(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    type(1,2,3,4)
TypeError: type() takes 1 or 3 arguments
>>> type(a)
<class 'tuple'>
>>> c=(1)       #튜플이 아니다.
>>> c
1
>>> type(c)
<class 'int'>
>>> 
>>> d=(1,)
>>> d
(1,)
>>> type(d) #,이 있으면 튜플이 될 수가 있다.
<class 'tuple'>

>>> e=1,
>>> e
(1,)
>>> tt=(1,2,3,4)
>>> tt_s= tt[0]+tt[1]+tt[2]+tt[3]
>>> tt_s
10
>>> tt_s2=0
>>> for i in tt:
	tt_s2 +=i

	
>>> tt_s2
10
>>> a=1,2,3
>>> b=3,3,3
>>> c=a+b
>>> c
(1, 2, 3, 3, 3, 3)  #패킹 튜플더
>>> a=1,2,3,4,5
>>> type(c)
<class 'tuple'>
>>> type(d)
<class 'tuple'>
>>> a=1,2,3,4
>>> q,w,e,r=a
>>> q
1
>>> w
2
>>> e
3
>>> r     #언패킹
4
>>> a=3
>>> b=7
>>> a,b=b,a
>>> sa
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    sa
NameError: name 'sa' is not defined
>>> a
7
>>> tmp = b,a
>>> a,b=tmp

>>> a
3
>>> a.index(3)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    a.index(3)
AttributeError: 'int' object has no attribute 'index'
>>> a=1,1,2,2,3,4,5
>>> a
(1, 1, 2, 2, 3, 4, 5)
>>> a.count(1)
2
>>> a.append(4)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a.append(4)
AttributeError: 'tuple' object has no attribute 'append'
>>> a
(1, 1, 2, 2, 3, 4, 5)
>>> b = list(a)
>>> b
[1, 1, 2, 2, 3, 4, 5]
#================================================================================
t=("회사정보","제품명","가격정보","출시일")
li = [":삼성전자",":갤럭시",":100원",":미정"]

for i in range(len(t)):
    print(t[i],"     ",li[i])

>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
회사정보       :삼성전자
제품명       :갤럭시
가격정보       :100원
출시일       :미정
#===============================================================================
#함수

>>> def test():
	print("Hello world~!!!")
>>> test()
Hello world~!!!

#===============================================================================
>>> def test(n):
	print("Hello wolrd")
	
>>> for n in range(5):
	test(n)

	
Hello wolrd
Hello wolrd
Hello wolrd
Hello wolrd
Hello wolrd

>>> def test2(num):
	print(num)

	
>>> test2(230)
230
#===============================================================================
>>> def test(a,b,c):
	print(a+b+c)

	
>>> test(1,2,3)
6

#===============================================================================
def test(a,b,c):
    print(a+b+c)

def test1(a,b,c):
    return a+b+c

test(1,2,3)

A= test1(4,5,6)
print("!!!",A,"!!!")
print("!!!",test1(4,5,6),"!!!")

=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
6
!!! 15 !!!
!!! 15 !!!

>>> a=5
>>> def test():
	print(a)

	
>>> test()
5
>>> a=5
>>> def test():
	a=4
	print(a)

	
>>> a
5
>>> test()
4
>>> a
5
>>> if(a==5):
	b=456

	
>>> b
456
>>> type(a)
<class 'int'>
>>> def test_g():
	global a
	a=4
	print(a)

	
>>> a
5
>>> test_g()
4
>>> a
4

>>> t=[1,2,3]
>>> def test_l():
	t.append(3)

	
>>> t
[1, 2, 3]
>>> test_l()
>>> t
[1, 2, 3, 3]
>>> def test_l2():
	t[2] = 999

	
>>> t
[1, 2, 3, 3]
>>> test_l2()
>>> t
[1, 2, 999, 3]

>>> def test_l3():
	global t#안전하게 코드 쓰고 싶을 때 사용한다.
	t[2] = 4

	
>>> t
[1, 2, 999, 3]
>>> test_l3()
>>> t
[1, 2, 4, 3]

#===============================================================================
a,b,c=10,20,30

def func(a,b,c):
    return a+b+c

for i in range(4):
    print(func(10+i,10+i,10+i))

=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
30
33
36
39


#==================즉 함수는 먼저 선언을 해줘야 함을 알 수가 있다.==============
a,b,c=10,20,30

for i in range(4):
    print(func(10+i,10+i,10+i))


def func(a,b,c):
    return a+b+c

=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day06/day_ex.py", line 42, in <module>
    print(func(10+i,10+i,10+i))
NameError: name 'func' is not defined

#함수 선언
#함수 호출
#위 두개의 차이점은 명백함으로 알아 놓는 것이 좋다.
#===============================================================================
#가위 바위 보 코드

#메뉴 출력
def print_menu():
    pass #아무일도 실행이 안됨

#가위 바위 보 입력
def ins_rcp():
    pass #이거 안써주면 오류가 난다.

#승부 결과 출력
def rcp_res:
    pass

#이길 때까지 반복
#컴퓨터는 무조건 바위

print_menu()
while(True):
    ins_rcp    

    res=rcp_res
    if(res==승리):
        break;
#==============================================================================
>>> test()
dddd
>>> def test1(n):
	for i in range(n):
		print(".d")

		
>>> def test1(a,b,c):
	print(a+b+c)

	
>>> def test(a,b,c):
	return a+b+c

>>> a= test1(1,2,3)
6
>>> a
>>> a = test2(1,2,3)
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    a = test2(1,2,3)
NameError: name 'test2' is not defined
>>> a = test2(1,2,3)
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    a = test2(1,2,3)
NameError: name 'test2' is not defined
>>> a
>>> def test3():
	print("hello")
	return
	print("world")

	
>>> test3()
hello
>>> a=1
>>> b=2
>>> c=3
>>> k=1
>>> m=2
>>> l=3
>>> test2(k,m,l)
6


>>> def swap(a,b):
	a,b=b,a

	
>>> k
1
>>> m
2
>>> def swap(a,b):
	return b,a

>>> k,m = swap
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    k,m = swap
TypeError: cannot unpack non-iterable function object
>>> k,m = swap(k,m)   #return이 한번만 된 것과 같다.
>>> k
2
>>> m
1
>>> type(swap(1,2))
<class 'tuple'>

#===============================================================================
def p_menu():
    print("""1. 학생등록
2.학생 점수 등록
3.학생 정보출력
4.학생순위순 표기
5.종료""")

def sel_1(name, age):
    stu_i.append([name,age,0])

def sel_3(num):
    print("%s번 학생 | 이름 : %s |나이: %s|점수: %s"
          %(n.stu_i[n][0],n.stu_i[n][1],n.stu_i[n][2]))

def sel_4():
    tmp = copy.deepcopy(stu_i)
    l = len(tmp)
    for i in range(l-1):
        for j in range(i+1,l):  #선택한것 뒤 부터, 끝까지 비교
            if tmp[i][2] < tmp[j][2]:   #선택한것이 더 크다면
                tmp[i],tmp[j] = tmp[j],tmp[i]
                #tmp = ls[i]       #더 작은값을 앞으로 이동
                #ls[i] = ls[j]
                #ls[j] = tmp
    print(tmp)
    
stu_i=[]

while(True):
    p_menu()
    
    sel = int(input())
    if(sel==1):
        name = input("학생의 이름을 등록하세요~!!!")
        age = input("학생의 나이를 입력하세요~!!!")
        sel_1(name,age)
        #stu_i.append([name,age,0])
    elif(sel==2):
        n = int(input("등록하고자 하는 학"))
        score= int(input("점수를 등록하세요~!!!"))
        sel_2(n,score)
        
    elif(sel==3):
        n= int(input("확인하고자 하는 학생 번호 입력:"))
        sel_3(n)
    elif(sel==4):
        sel_4()
        print("학생 순위순 표기")
        for i in range(n):
            if(score>n.stu_i[n][2]):
                tmp = score
                score = n
                n=tmp
        print("%s번 학생 | 이름 : %s |나이: %s|점수: %s"%(n.stu_i[n][0],n.stu_i[n][1],n.stu_i[n][2]))
    else:
        break;
#===============================================================================
def res(a,b):
    return a+b


if(res(8,3)%2==0):
    print("True")
elif(res(8,3)%2==1):
    print("False")

=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
False


def res(a,b):
    return a+b


if(res(5,5)%2==0):
    print("True")
elif(res(5,5)%2==1):
    print("False")

=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
True

#==============================================================================
def res(num):
    if(num%2==0):
        return True
    elif(num%2==1):
        return False
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
>>> if(res(5)):
	pirnt("ddd")
#===============================================================================
>>> def test(*v):
	for i in v:
		print(i)

		
>>> test(1,33,4,5,6,6)
1
33
4
5
6
6
>>> def test(*v):
	print(v)
	for i in v:
		print(i)

		
>>> test(1,2,34,5,435,4)
(1, 2, 34, 5, 435, 4)
1
2
34
5
435
4
#===============================================================================
def sum_m(*v):
	res01=0
	for i in v:
		res01=res01+i
	return res01

def avg_m(*v):
    res=01
    j=0for i in v:
        res = res+i
        j+=1
    return res/j

def rev(*v):
    tmp = list(v)
    return tuple(tmp,rev())

