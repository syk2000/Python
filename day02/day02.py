>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!


import antigravity #웹사이트가 나온다. 파이썬의 장점부분이 나옴

>>> round(1/3)
0
>>> round(1/3,1)
0.3
>>> round(1/3,3)
0.333
>>> print("1/3 = %f"%(round(1/3,3)))
1/3 = 0.333000


>>> floor_h = 500.23
>>> avg=260
>>> cnt=14
>>> build_h=floor_h+(avg*(cnt-1))/100
>>> build_h = round(build_h,3)
>>> print("건물의 높이는",build_h,"m 입니다.")
건물의 높이는 534.03 m 입니다.
#====================================================
>>> build_h=floor_h+(avg*(cnt-1))
>>> build_h = round(build_h/100,3)
>>> print("건물의 높이는",build_h,"m 입니다.")
건물의 높이는 534.03 m 입니다.

>>> type("dd")
<class 'str'>

>>> a=1
>>> type(a)
<class 'int'>

>>> print("%s"%(type(a)))
<class 'int'>

>>> type(a)
<class 'float'>

>>> a='a'
>>> type(a)
<class 'str'>

>>> a=False
>>> type(a)
<class 'bool'>

id(a)
140728845252976
>>> a=2
>>> id(a)
140728845784128
>>> id(1)
140728845784096
>>> id(5-4)
140728845784096
>>> id(9-4)
140728845784224

>>> "d"+str(3)
'd3'
>>> 2+"3"
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    2+"3"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 2+int("3")
5

>>> type(2);type(str(2));type(float(2))
<class 'int'>
<class 'str'>
<class 'float'>

>>> su+int(num)
200

>>> print(su+int(num))
200

>>> float(num)+float(flt)
101.111

>>> print(su+float(flt))
101.111

>>> num+num
'100100'
>>> print(str(su)+num)
100100

#===========================
>>> su = 100
>>> num = '100'
>>> flt="1.111"

>>> su+=100
>>> su
200

>>> num=101.111
>>> num
101.111

>>> print(num+num)
100100

print(n=10) #오류가 난다.
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print(n=10)
TypeError: 'n' is an invalid keyword argument for print()


>>> a = input()
123
>>> a
'123'

>>> name = input("이름을 알려주세요~!!!") #Scanner과 같은 것 
이름을 알려주세요~!!!홍길동
>>> name
'홍길동'

>>> name=input("이름을 알려주세요");age=input("나이를 알려주세요~!!! ")
이름을 알려주세요홍길동
나이를 알려주세요~!!! 20

>>> print(name,"님의 나이는",age ,"입니다.")
홍길동 님의 나이는 20 입니다.


name=input("이름을 알려주세요")age=input("나이를 알려주세요~!!! ")
print(name,"님의 나이는",age ,"입니다.")

이름을 알려주세요 홍길동
나이를 알려주세요~!!! 25
 홍길동 님의 나이는 25 입니다.

print("%s님의 나이는 %s살 입니다."%(name,age))
 홍길동님의 나이는 25살 입니다.

 #==============================================================================

print("두수를 입력해주세요~!!!\n")
res=input()res1=input()
print("두수의합",(res+res1))
두수를 입력해주세요~!!!

5 2
25
두수의합 5 225

>>>print("두수를 입력해주세요~!!!\n")
>>>res=input();res1=input();sum=int(res)+int(res1)
>>>print("두수의 합: ",int(sum))
							      
2
5
두수의 합: 7

>>> sum = int(res)+int(res1)
							      
>>> print("%d"%(sum))
							      
7


>>> min = int(res-res1)
>>> mul = int(res)*int(res1)							      
>>> div=int(res)/int(res1)

>>> print("+:",sum)print("-:",min)print("*:",mul)print("/:",div)
							      
+: 7
-: -3
*: 10
/: 0.4

>>>born = int(input("태어난 연도를 입력하세요~!!!"))
year=int(input("올해 연도를 입력하세요"))
res = year-born; print("당신의 나이는 %s살입니다."%(res))
							      
#태어난 연도를 입력하세요~!!!2000
#올해 연도를 입력하세요2019
#당신의 나이는 19살입니다.

first = float(input("첫번째 물건의 무게를 입력하세요~!!!"))
second=float(input("두번째 물건의 무게를 입력하세요~!!!"))
sum = first+secondprint("현재 엘레베이터에 허용무게는 %.2f 입니다."%(sum))
							      
#첫번째 물건의 무게를 입력하세요~!!!64.27
#두번째 물건의 무게를 입력하세요~!!!75.25
#현재 엘레베이터에 허용무게는 139.52 입니다.

name = input("학생이름:")
sc = int(input("국어 점수:"))
sc1=int(input("영어점수:"))
sc2=int(input("수학 점수:"))
sum=sc+sc1+sc2
avg=float(sum)/5
print("=======================학생 정보==========================\n")
print("이름\t국어\t영여\t수학\t합계\t평균\n%s\t%d\t%d\t%d\t%d\t%.2f"%(name,sc,sc1,sc2,sum,float(avg)))
#================================================
num=int(input());num01=int(input())
res=int(num)*int(num01)
res01=int(num01%10)*int(num)
res02=int(num01/10)*int(num)
res03 = int(num01/100)*int(num)
sum = int(num)*int(num01)
print("%s \n%s \n%s \n%s \n%s"%(res,res01,res02,res03,sum))

472
385
181720 
2360 
17936 
1416 
181720

#===============================================================================
su1 = 3.1;su2=3

print("su1>=su2",(su1>=su2))
print("su1<=su2",(su1<=su2))
print("su1==su2",(su1==su2))
print("su1!=su2",(su1!=su2))

su1>=su2 True
su1<=su2 False
su1==su2 False
su1!=su2 True
'''print(su-=1) 보이지 않는다.'''
#==============================================================================
not(False)  #true
not(False or True)#true
not(False and True)#false
not(0)              #true
not(1)              #false

#=============================================================================
>>> bin(255)
																									     
'0b11111111'
>>> bin(~255)
																									     
'-0b100000000'

>>> ~255
																									     
-256

>>> 0b0101010101
																									     
341
>>> bin(341)
																									     
'0b101010101'
>>> bin(~341)
																									     
'-0b101010110'
>>> bin(~0b0101010101)
																									     
'-0b101010110'

>>> a=0b11110000
																									     
>>> b=0b11111111
																									     
>>> bin(a|b)
																									     
'0b11111111'
>>> c=0b00001111
																									     
>>> bin(a|c)
																									     
'0b11111111'
>>> bin(a&b)
																									     
'0b11110000' 
>>> d=0b10011101
																									     
>>> bin(a&d)
																									     
'0b10010000'
>>> bin(a|d)
																									     
'0b11111101'
>>> bin(0^0)
																									     
'0b0'
>>> bin(0^1)
																									     
'0b1'
>>> bin(1^1)
																									     
'0b0'
>>> bin(0^1)
																									     
'0b1'
>>> bin(1^1)
																									     
'0b0'
>>> bin(0b111111111^0b1011011)
																									     
'0b110100100'
>>> a=5
																									     
>>> b=89
																									     
>>> b^5
																									     
92
>>> 92^5 #겹치면 뒤집히고 아니면 안뒤집힌다.
																									     
89
>>> tmp = a       #swap하는 경우 즉 뒤바뀌는 경
																									     
>>> a=b
																									     
>>> b=tmp
																									     
>>> a
																									     
57
>>> b
																									     
46

>>> a=0b11110000																									     
>>> a>>2																									     
60
>>> bin(a>>2)	#2의 n승하는 것과 같다.																								     
'0b111100'







