>>> a= 123456789
>>> b= 123456789
>>> a==b
True
>>> a is b
False
>>> c=12
>>> d=12
>>> c is d
True
>>> id(a)
2613711410224
>>> id(b)
2613711410192
>>> id(c)
140728344958336
>>> id(d)
140728344958336
#큰수는 주소가 다르지만 작은 수이면 주소가 같다.

#======================================================================
age= int(input("나이를 입력하세요~!!!"))
year = int(input("년도를 입력하세요~!!!"))
result = int(year)-2000-int(age)
res = int(year)-2000

if(year>=2000 & res>=age):
    print("두사람의 나이차이는: %s\n"%(result))
else:
    print("맞지 않습니다.")

================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
나이를 입력하세요~!!!19
년도를 입력하세요~!!!2020
두사람의 나이차이는: 1

>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
나이를 입력하세요~!!!15
년도를 입력하세요~!!!2020
두사람의 나이차이는: 5

>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
나이를 입력하세요~!!!15
년도를 입력하세요~!!!1999
맞지 않습니다.

#============================================================================
num1 =10
num2 = 5

if(num1>num2):
    print("num1 is larger than num2")
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================

num1 is larger than num2
#===============================================================================
num1 =10
num2 = 51

if(num1>num2):
    print("num1 is larger than num2")
if(num2>num1):
    print("num2 is larger than num1")

================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
num2 is larger than num1
#=================================================================================
num1 =int(input())
num2 = int(input())

if(num1>num2):
    print("num1 is larger than num2")
if(num2>num1):
    print("num2 is larger than num1")
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
15
20
num2 is larger than num1

#==============================================================================
num1 =int(input())
num2 = int(input())

if(num1%2==0):
    print("num1은 짝수")
else:
    print("num1은 홀수")

if(num2%2==0):
    print("num2은 짝수")
else:
    print("num2은 홀수")

================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
25
20
num1은 홀수
num2은 짝수

#===============================================================================
date = input("날짜를 8자리로 입력하세요~!!! 예)20191225")
year = int(date) //10000
m = (int(date)//100)%100


if(year%4==0 & year%100!=0 or year%400==0):
    if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
        print("윤년입니다~!!!!")
        print("윤달입니다~!!!")
        print("이달은 31일 까지 있습니다.")
    elif(m==4 or m==6 or m==9 or m==11):
        print("윤년입니다~!!!!")
        print("윤달입니다~!!!")
        print("이달은 30일 까지 있습니다.")
    elif(m==2):
        print("윤년입니다~!!!!")
        print("윤달입니다~!!!")
        print("28일 까지 있습니다.")
else:
    if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
        print("윤년이 아닙니다")
        print("윤달이 아닙니다.")
        print("이달은 31일 까지 있습니다.")
    elif(m==4 or m==6 or m==9 or m==11):
        print("윤년이 아닙니다")
        print("윤달이 아닙니다.")
        print("이달은 30일 까지 있습니다.")
    elif(m==2):
        print("윤년이 아닙니다")
        print("윤달이 아닙니다.")
        print("29일 까지 있습니다.")

================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
날짜를 8자리로 입력하세요~!!! 예)2019122520000601
윤년입니다~!!!!
윤달입니다~!!!
이달은 30일 까지 있습니다.

#=========================================================================
date = input("날짜를 8자리로 입력하세요~!!! 예)20191225")
year = int(date) //10000
m = (int(date)//100)%100


if(year%400==0):
    state =True
elif(year % 4 ==0 and year %100==0):
    state = False
elif(year%4==0):
    state =True
else:
    state = False
print("%d년은 "%(year), end='')
if(state):
    print("윤년입니다.")
else:
    print("평년입니다.")

#==========================================================================
day=int(input("날짜를 입력하세요~!!!"))

if(day-1%7==0):
    print("월요일")
elif(day-1%7==1):
    print("화요일")
elif(day-1%7==2):
    print("수요일")
elif(day-1%7==3):
    print("목요일")
elif(day-1%7==4):
    print("금요일")
elif(day-1%7==5):
    print("토요일")
elif(day-1%7==6):
    print("일요일")
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
날짜를 입력하세요~!!!7
일요일

#===============================================================================
#세수 비교 
n= int(input())
n1= int(input())
n2= int(input())

if(n>n1 and n>n2):
    if(n1>n2):
        print(n,n1,n2)
    else:
        print(n,n2,n1)
elif(n1>n2 and n1>n):
    if(n>n2):
        print(n1,n,n2)
    else:
        print(n1,n2,n)
elif(n2>n1 and n2>n):
    if(n1>n):
        print(n2,n1,n)
    else:
        print(n2,n,n1)
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
2
5
7
7 5 2

#=============================================================================
#두수를 입력받아 큰수가 짝수이면 출
n= int(input())
n1= int(input())

if(n>n1):
    if(int(n)%2==0):
        print(n)
else:
    if(int(n1)%2==0):
        print(n1)

================ RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
5
10
10

#============================================================================
#두수를 입력받아 합이 짝수이고 3의 배수인 
n= int(input())
n1= int(input())
res = int(n)+int(n1)
if(int(res)%2==0 and int(res)%3==0):
    print(res)

================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
15
15
30

================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
20
21

# 절대값을 구하는 프로그램
n= int(input())
if(n>=0):
    print(n)
else:
    res = int(n)*-1
    print(res)

#=============================================================================
    #1GB = 1024MB
#1MB = 1024KB
#1KB = 1024B

gb = int(input("용량은?(GB)"))
sel = int(input("""
1.byte
2.kbyte
3.Mbyte
선택 : """ ))

if(sel ==1):
    res = str(gb*1024*1024*1024)+"byte"
    #res = str(gb*(1024**3))+"byte"
    print(res)
elif(sel==2):
    res = str(gb*1024*1024)+"kbyte"
    print(res)

elif(sel==3):
    res = str(gb*1024)+"Mbyte"
    print(res)

================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
용량은?(GB)2

1.byte
2.kbyte
3.Mbyte
선택 : 3
2048Mbyte

#==============================================================================
pid_id = "test"
pid_pw = "pw"

new_id=input()
old_id=input()
if(old_id ==new_id):
    if(old_pw ==new_pw):
        print("인증성공")
    else:
        print("비밀번호 틀림")
else:
    print("아이디 입니다.")
#==============================================================================
name = input("이름을 입력하세요~!!!")
grade = input("학번을 입력하세요")
sc= int(input())
sc1= int(input())
sc2= int(input())

res= int(sc)+int(sc1)+int(sc2)
avg = int(res)/3


if(avg>=90):
    print("%s\n%s\n%s\n%s\nA"%(name,grade,res,avg))
elif(avg>=80):
    print("%s\n%s\n%s\n%s\nB"%(name,grade,res,avg))
elif(avg>=70):
    print("%s\n%s\n%s\n%s\nC"%(name,grade,res,avg))
elif(avg>=60):
    print("%s\n%s\n%s\n%s\nD"%(name,grade,res,avg))
else:
    print("%s\n%s\n%s\n%s\nF"%(name,grade,res,avg))

================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
이름을 입력하세요~!!!홍길동
학번을 입력하세요201974465
78
98
67
홍길동
201974465
243
81.0
B











