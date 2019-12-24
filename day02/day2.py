Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
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
>>> import antigravity
>>> "%.3f"%(1/3)
'0.333'
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
>>> 
>>> build_h=floor_h+(avg*(cnt-1))
>>> build_h = round(build_h,3)
>>> print("건물의 높이는",build_h,"m 입니다.")
건물의 높이는 3880.23 m 입니다.
>>> build_h=floor_h+(avg*(cnt-1))/100
>>> build_h = round(build_h,3)
>>> print("건물의 높이는",build_h,"m 입니다.")
SyntaxError: multiple statements found while compiling a single statement
>>> build_h=floor_h+(avg*(cnt-1))/100
>>> build_h = round(build_h,3)
>>> print("건물의 높이는",build_h,"m 입니다.")
건물의 높이는 534.03 m 입니다.
>>> type("dd")
<class 'str'>
>>> a=1
>>> type(a)
<class 'int'>
>>> print("%s"%(type(a)))
<class 'int'>
>>> a=3.1
>>> type(a)
<class 'float'>
>>> a='a'
>>> type(a)
<class 'str'>
>>> a=b
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a=b
NameError: name 'b' is not defined
>>> a='b'
>>> type(a)
<class 'str'>
>>> a= FALSE
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a= FALSE
NameError: name 'FALSE' is not defined
>>> a= TURE
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a= TURE
NameError: name 'TURE' is not defined
>>> a=False
>>> type(a)
<class 'bool'>
>>> id(a)
140728845252976
>>> id(a)
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
>>> su = 100
>>> num = '100'
>>> flt="1.111"
>>> type(flt)
<class 'str'>
>>> id(su+num)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    id(su+num)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> id(num+num)
2470440350472
>>> num+flt
'1001.111'
>>> print(num+flt)
1001.111
>>> num+num
'100100'
>>> print(num+num)
100100
>>> print(num+num)
100100
>>> num+=1.111
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    num+=1.111
TypeError: can only concatenate str (not "float") to str
>>> num=101.111
>>> num
101.111
>>> su+=100
>>> su
200
>>> su=100
>>> num='100'
>>> su+int(num)
200
>>> num+num
'100100'
>>> float(num)+float(flt)
101.111
>>> print(n=10)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print(n=10)
TypeError: 'n' is an invalid keyword argument for print()
>>> print(su+(int)num)
SyntaxError: invalid syntax
>>> print(su+int(num))
200
>>> print(su+float(flt))
101.111
>>> print(str(su)+num)
100100
>>> a = input()
123
>>> a
'123'
>>> type(a)
<class 'str'>
>>> name = input("이름을 알려주세요~!!!")
이름을 알려주세요~!!!sfsdfsdf
>>> name = input("이름을 알려주세요~!!!")
이름을 알려주세요~!!!홍길동
>>> name
'홍길동'
>>> name=input("이름을 알려주세요\n")
이름을 알려주세요
sdaf
>>> name+=input("나이를 알려주세요~!!! ")
나이를 알려주세요~!!! 20
>>> ㅜ믇
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    ㅜ믇
NameError: name 'ᅮ믇' is not defined
>>> name
'sdaf20'
>>> name=input("이름을 알려주세요");age=input("나이를 알려주세요~!!! ")
이름을 알려주세요홍길동
나이를 알려주세요~!!! 20
>>> print(name,"님의 나이는",age 입니다.)
SyntaxError: invalid syntax
>>> >>> print(name,"님의 나이는",age ,"입니다.")
SyntaxError: invalid syntax
>>> print(name,"님의 나이는",age ,"입니다.")
홍길동 님의 나이는 20 입니다.
>>> name=input("이름을 알려주세요");age=input("나이를 알려주세요~!!! ");print(name,"님의 나이는",age ,"입니다.")
이름을 알려주세요 홍길동
나이를 알려주세요~!!! 25
 홍길동 님의 나이는 25 입니다.
>>> res,res1 = input("두 수를 입력해주세요~!!!"); print()
두 수를 입력해주세요~!!!2 5
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    res,res1 = input("두 수를 입력해주세요~!!!"); print()
ValueError: too many values to unpack (expected 2)
>>> print("두수의 합은",(res+res1))
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    print("두수의 합은",(res+res1))
NameError: name 'res' is not defined
>>> print("두수를 입력해주세요~!!!\n"); res=input();res1=input();print("두수의합",(res+res1))
두수를 입력해주세요~!!!

5 2
25
두수의합 5 225
>>> 
>>> print("%s님의 나이는 %s살 입니다."%(name,age))
 홍길동님의 나이는 25살 입니다.
>>> print("두수의 합:%d"%(res+res1))
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    print("두수의 합:%d"%(res+res1))
TypeError: %d format: a number is required, not str
>>> sum=res+res1
>>> print("두수의 합:%d"%(sum))
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    print("두수의 합:%d"%(sum))
TypeError: %d format: a number is required, not str
>>> print("두수를 입력해주세요~!!!\n"); res=input();res1=input();sum=res+res1;print("두수의 합: %s",sum)
두수를 입력해주세요~!!!

5
2
두수의 합: %s 52
>>> print("두수를 입력해주세요~!!!\n"); res=input();res1=input();sum=res+res1;print("두수의 합: %d",sum)
두수를 입력해주세요~!!!

2
5
두수의 합: %d 25
>>> type(sum)
<class 'str'>
>>> type(res)
<class 'str'>
>>> print("두수를 입력해주세요~!!!\n"); res=input();res1=input();sum=res+res1;print("두수의 합: %s",%sum)
SyntaxError: invalid syntax
>>> print("두수를 입력해주세요~!!!\n"); res=input();res1=input();sum=res+res1;print("두수의 합: %s",%(sum))
SyntaxError: invalid syntax
>>> print("두수를 입력해주세요~!!!\n"); res=input();res1=input();print("두수의 합: %s",%(res+res1)
							      
SyntaxError: invalid syntax
>>> print("두수를 입력해주세요~!!!\n"); res=input();res1=input();print("두수의 합: %s",(res+res1)
							      5
							      
SyntaxError: invalid syntax
>>> print("두수를 입력해주세요~!!!\n"); res=input();res1=input();sum=res+res1;print("두수의 합: %s",sum)
							      
두수를 입력해주세요~!!!

2
5
두수의 합: %s 25
>>> print("두수를 입력해주세요~!!!\n"); res=input();res1=input();sum=int(res)+int(res1);print("두수의 합: %d",(int)sum)
							      
SyntaxError: invalid syntax
>>> type(sum)
							      
<class 'str'>
>>> res=input();res1=input();sum=int(res)+int(res1);print("두수의 합: %d",int(sum))
							      
2
5
두수의 합: %d 7
>>> res=input();res1=input();sum=int(res)+int(res1);print("두수의 합: %s",int(sum))
							      
2
5
두수의 합: %s 7
>>> res=input();res1=input();sum=int(res)+int(res1);print("두수의 합: ",int(sum))
							      
2
5
두수의 합:  7
>>> res=input();res1=input();sum=int(res)+int(res1);print("두수의 합: %d",%int(sum))
							      
SyntaxError: invalid syntax
>>> res=input();res1=input();sum=int(res)+int(res1);print("두수의 합: ",%(int(sum)))
							      
SyntaxError: invalid syntax
>>> res=input();res1=input();sum=int(res)+int(res1);print("두수의 합: %d",%(int(sum)))
							      
SyntaxError: invalid syntax
>>> sum = int(res)+int(res1)
							      
>>> print("%d"%(sum))
							      
7
>>> print("+:",???)
							      
SyntaxError: invalid syntax
>>> print("+:",???)print("-:",???)print("*:",???)print("/:",???)
							      
SyntaxError: invalid syntax
>>> min = int(res-res1)
							      
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    min = int(res-res1)
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> min = int(res)-int(res1)
							      
>>> print(min)
							      
-3
>>> mul = int(res)*int(res1)
							      
>>> div=int(res)/int(res1)
							      
>>> print("+:",sum);print("-:",min);print("*:",mul);print("/:",div)
							      
+: 7
-: -3
*: 10
/: 0.4
>>> born = int(input("태어난 연도를 입력하세요~!!!"));year=int(input("올해 연도를 입력하세요"));res = year-born; print("당신의 나이는 %s살입니다."%(res))
							      
태어난 연도를 입력하세요~!!!2000
올해 연도를 입력하세요2019
당신의 나이는 19살입니다.
>>> born = int(input("태어난 연도를 입력하세요~!!!"));
							      
태어난 연도를 입력하세요~!!!2000
>>> first = float(input("첫번째 물건의 무게를 입력하세요~!!!"));second=float(input("두번째 물건의 무게를 입력하세요~!!!")); sum = first+second;print("현재 엘레베이터에 허용무게는 %s 입니다."%(sum))
							      
첫번째 물건의 무게를 입력하세요~!!!64.27
두번째 물건의 무게를 입력하세요~!!!75.25
현재 엘레베이터에 허용무게는 139.51999999999998 입니다.
>>> first = float(input("첫번째 물건의 무게를 입력하세요~!!!"));second=float(input("두번째 물건의 무게를 입력하세요~!!!")); sum = first+second;print("현재 엘레베이터에 허용무게는 %.2s 입니다."%(sum))
							      
첫번째 물건의 무게를 입력하세요~!!!64.27
두번째 물건의 무게를 입력하세요~!!!75.25
현재 엘레베이터에 허용무게는 13 입니다.
>>> first = float(input("첫번째 물건의 무게를 입력하세요~!!!"));second=float(input("두번째 물건의 무게를 입력하세요~!!!")); sum = first+second;print("현재 엘레베이터에 허용무게는 %.2f 입니다."%(sum))
							      
첫번째 물건의 무게를 입력하세요~!!!64.27
두번째 물건의 무게를 입력하세요~!!!75.25
현재 엘레베이터에 허용무게는 139.52 입니다.
>>> name = input("학생이름:"); sc = int(input("국어 점수:"));sc1=int(input("영어점수:"));sc2=int(input("수학 점수:"));int(sum)=sc+sc1+sc2;float(avg)=float(sum)/5;pirnt("=======================학생 정보==========================\n이름  국어  영어  수학  합계  평균\n%s  %d %d %d %d %.2f"%(name,sc,sc1,sc2,sum,avg));
							      
SyntaxError: can't assign to function call
>>> name = input("학생이름:"); sc = int(input("국어 점수:"));sc1=int(input("영어점수:"));sc2=int(input("수학 점수:"));int(sum)=sc+sc1+sc2;float(avg)=float(sum)/float(5);pirnt("=======================학생 정보==========================\n이름  국어  영어  수학  합계  평균\n%s  %d %d %d %d %.2f"%(name,sc,sc1,sc2,sum,avg));
							      
SyntaxError: can't assign to function call
>>> name = input("학생이름:"); sc = int(input("국어 점수:"));sc1=int(input("영어점수:"));sc2=int(input("수학 점수:"));int(sum)=sc+sc1+sc2;float(avg)=sum/5;pirnt("=======================학생 정보==========================\n이름  국어  영어  수학  합계  평균\n%s  %d %d %d %d %.2f"%(name,sc,sc1,sc2,sum,avg));
							      
SyntaxError: can't assign to function call
>>> name = input("학생이름:"); sc = int(input("국어 점수:"));sc1=int(input("영어점수:"));sc2=int(input("수학 점수:"));sum=sc+sc1+sc2;float(avg)=float(sum)/5;pirnt("=======================학생 정보==========================\n이름  국어  영어  수학  합계  평균\n%s  %d %d %d %d %.2f"%(name,sc,sc1,sc2,sum,avg));
							      
SyntaxError: can't assign to function call
>>> name = input("학생이름:"); sc = int(input("국어 점수:"));sc1=int(input("영어점수:"));sc2=int(input("수학 점수:"));sum=sc+sc1+sc2;float(avg)=float(sum)/5
							      
SyntaxError: can't assign to function call
>>> name = input("학생이름:")
							      
학생이름:홍길동
>>> sc = int(input("국어 점수:"))
							      
국어 점수:85
>>> sc1=int(input("영어점수:"))
							      
영어점수:70
>>> sc2=int(input("수학 점수:"))
							      
수학 점수:85
>>> sum=sc+sc1+sc2
							      
>>> print(sum)
							      
240
>>> float(avg)=float(sum)/5
							      
SyntaxError: can't assign to function call
>>> float(avg)=float(sum)/float(5)
							      
SyntaxError: can't assign to function call
>>> avg=float(sum)/float(5)
							      
>>> name = input("학생이름:"); sc = int(input("국어 점수:"));sc1=int(input("영어점수:"));sc2=int(input("수학 점수:"));sum=sc+sc1+sc2;avg=float(sum)/5;pirnt("=======================학생 정보==========================\n이름  국어  영어  수학  합계  평균\n%s  %d %d %d %d %.2f"%(name,sc,sc1,sc2,sum,avg));
							      
학생이름:홍길동
국어 점수:85
영어점수:90
수학 점수:50
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    name = input("학생이름:"); sc = int(input("국어 점수:"));sc1=int(input("영어점수:"));sc2=int(input("수학 점수:"));sum=sc+sc1+sc2;avg=float(sum)/5;pirnt("=======================학생 정보==========================\n이름  국어  영어  수학  합계  평균\n%s  %d %d %d %d %.2f"%(name,sc,sc1,sc2,sum,avg));
NameError: name 'pirnt' is not defined
>>> name = input("학생이름:"); sc = int(input("국어 점수:"));sc1=int(input("영어점수:"));sc2=int(input("수학 점수:"));sum=sc+sc1+sc2;avg=float(sum)/5;print("=======================학생 정보==========================\n이름  국어  영어  수학  합계  평균\n%s  %d %d %d %d %.2f"%(name,sc,sc1,sc2,sum,avg));
							      
학생이름:홍길동
국어 점수:85
영어점수:90
수학 점수:70
=======================학생 정보==========================
이름  국어  영어  수학  합계  평균
홍길동  85 90 70 245 49.00
>>> name = input("학생이름:");
sc = int(input("국어 점수:"));
sc1=int(input("영어점수:"));
sc2=int(input("수학 점수:"));
sum=sc+sc1+sc2;
avg=float(sum)/5;
print("=======================학생 정보==========================\n");
print("이름\t국어\t영여\t수학\t합계\t평균\n%s\t%d\t%d\t%d\t%d\t%.2f"%(name,sc,sc1,sc2,sum,float(avg));
      
SyntaxError: multiple statements found while compiling a single statement
>>> name = input("학생이름:")
sc = int(input("국어 점수:"))
sc1=int(input("영어점수:"))
sc2=int(input("수학 점수:"))
sum=sc+sc1+sc2
avg=float(sum)/5
print("=======================학생 정보==========================\n")
print("이름\t국어\t영여\t수학\t합계\t평균\n%s\t%d\t%d\t%d\t%d\t%.2f"%(name,sc,sc1,sc2,sum,float(avg))
      
SyntaxError: multiple statements found while compiling a single statement
>>> name = input("학생이름:");sc = int(input("국어 점수:"));sc1=int(input("영어점수:"));sc2=int(input("수학 점수:"));sum=sc+sc1+sc2;avg=float(sum)/5;print("=======================학생 정보==========================\n");print("이름\t국어\t영여\t수학\t합계\t평균\n%s\t%d\t%d\t%d\t%d\t%.2f"%(name,sc,sc1,sc2,sum,float(avg));
																									     
SyntaxError: invalid syntax
>>> name = input("학생이름:");sc = int(input("국어 점수:"));sc1=int(input("영어점수:"));sc2=int(input("수학 점수:"));sum=sc+sc1+sc2;avg=float(sum)/5;print("=======================학생 정보==========================\n이름\t국어\t영여\t수학\t합계\t평균\n%s\t%d\t%d\t%d\t%d\t%.2f"%(name,sc,sc1,sc2,sum,float(avg)))
																									     
학생이름:홍길동
국어 점수:95
영어점수:90
수학 점수:75
=======================학생 정보==========================
이름	국어	영여	수학	합계	평균
홍길동	95	90	75	260	52.00
>>> name = input("학생이름:");
sc = int(input("국어 점수:"));
sc1=int(input("영어점수:"));
sc2=int(input("수학 점수:"));
sum=sc+sc1+sc2;
avg=float(sum)/5;
print("=======================학생 정보==========================\n");
print("이름\t국어\t영여\t수학\t합계\t평균\n%s\t%d\t%d\t%d\t%d\t%.2f"%(name,sc,sc1,sc2,sum,float(avg)))
																									     
SyntaxError: multiple statements found while compiling a single statement
>>> name = input("학생이름:");sc = int(input("국어 점수:"));sc1=int(input("영어점수:"));sc2=int(input("수학 점수:"));sum=sc+sc1+sc2;avg=float(sum)/5;print("=======================학생 정보==========================\n");print("이름\t국어\t영여\t수학\t합계\t평균\n%s\t%d\t%d\t%d\t%d\t%.2f"%(name,sc,sc1,sc2,sum,float(avg)))
																									     
학생이름:홍길동
국어 점수:85
영어점수:90
수학 점수:75
=======================학생 정보==========================

이름	국어	영여	수학	합계	평균
홍길동	85	90	75	250	50.00
>>> 
==================== RESTART: D:/평일_파이썬_신윤규/day02/ex01.py ====================

==================== RESTART: D:/평일_파이썬_신윤규/day02/ex01.py ====================
2
5
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day02/ex01.py", line 2, in <module>
    res=int(num)*int(num1);res01=int(num01%10)*int(num)
NameError: name 'num1' is not defined
>>> 
==================== RESTART: D:/평일_파이썬_신윤규/day02/ex01.py ====================
472
385
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day02/ex01.py", line 2, in <module>
    res=int(num)*int(num1);res01=int(num01%10)*int(num)
NameError: name 'num1' is not defined
>>> 
==================== RESTART: D:/평일_파이썬_신윤규/day02/ex01.py ====================

==================== RESTART: D:/평일_파이썬_신윤규/day02/ex01.py ====================
472
385
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day02/ex01.py", line 2, in <module>
    res=int(num)*int(num1)
NameError: name 'num1' is not defined
>>> 
==================== RESTART: D:/평일_파이썬_신윤규/day02/ex01.py ====================
472
385
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day02/ex01.py", line 2, in <module>
    res=int(num)*int(num1)
NameError: name 'num1' is not defined
>>> 
==================== RESTART: D:/평일_파이썬_신윤규/day02/ex01.py ====================
472
385
181720 2360 17936 1416 181720
>>> 
==================== RESTART: D:/평일_파이썬_신윤규/day02/ex01.py ====================
472
385
181720 
2360 
17936 
1416 
181720
>>> 
==================== RESTART: D:/평일_파이썬_신윤규/day02/ex01.py ====================
su1>=su2 True
su1<=su2 False
su1==su2 False
su1!=su2 True
>>> 
==================== RESTART: D:/평일_파이썬_신윤규/day02/ex01.py ====================
>>> 
==================== RESTART: D:/평일_파이썬_신윤규/day02/ex01.py ====================
>>> true
																									     
Traceback (most recent call last):
  File "<pyshell#224>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> false
																									     
Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    false
NameError: name 'false' is not defined
>>> 
==================== RESTART: D:/평일_파이썬_신윤규/day02/ex01.py ====================
>>> 
==================== RESTART: D:/평일_파이썬_신윤규/day02/ex01.py ====================
>>> bin(255)
																									     
'0b11111111'
>>> bin(~255)
																									     
'-0b100000000'
>>> -256
																									     
-256
>>> ~255
																									     
-256
>>> 0b010101
																									     
21
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
>>> bin(0b111111111^0b1011011)
																									     
'0b110100100'
>>> a=5
																									     
>>> b=89
																									     
>>> b^5
																									     
92
>>> 92^5
																									     
89
>>> a=46
																									     
>>> b=57
																									     
>>> tmp = a
																									     
>>> a=b
																									     
>>> b=tmp
																									     
>>> a
																									     
57
>>> b
																									     
46
>>> a=46
																									     
>>> b=57
																									     
>>> a^b
																									     
23
>>> a
																									     
46
>>> a=a^b
																									     
>>> b=a^b
																									     
>>> a
																									     
23
>>> b
																									     
46
>>> 
																									     
>>> 
																									     
>>> 
																									     
>>> 
																									     
>>> 
																									     
>>> 
																									     
>>> 
																									     

>>> 
																									     

>>> 
																									     
>>> 
																									     
>>> 
																									     

>>> 
																									     

>>> 
																									     
>>> 
																									     
>>> 
																									     
>>> a=2
																									     
>>> b=1
																									     
>>> a=a^b
																									     
>>> a
																									     
3
>>> b=b^a
																									     
>>> b
																									     
2
>>> a=0b11110000
																									     
>>> a>>2
																									     
60
>>> bin(a>>2)
																									     
'0b111100'
>>> 
