Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
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
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
나이를 입력하세요~!!!20
년도를 입력하세요~!!!2020
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 5, in <module>
    print("두사람의 나이차이는: \n"%(result))
TypeError: not all arguments converted during string formatting
>>> 
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
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
num1 is larger than num2
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
num2 is larger than num1
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
15
20
num2 is larger than num1
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================20
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 1, in <module>
    num1 =int(input())
ValueError: invalid literal for int() with base 10: '================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================20'
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
25
20
num1은 홀수
num2은 짝수
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
25
20
num1은 홀수 num2는 홀수
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
날짜를 8자리로 입력하세요~!!! 예)2019122520000601
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 2, in <module>
    year = date //10000
TypeError: unsupported operand type(s) for //: 'str' and 'int'
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
날짜를 8자리로 입력하세요~!!! 예)2019122520000601
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 2, in <module>
    year = date //10000
TypeError: unsupported operand type(s) for //: 'str' and 'int'
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
날짜를 8자리로 입력하세요~!!! 예)2019122520000601
윤년이 아닙니다.
윤달이 아닙니다.
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
날짜를 8자리로 입력하세요~!!! 예)2019122520000601
윤년이 아닙니다.
윤달이 아닙니다.
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
날짜를 8자리로 입력하세요~!!! 예)2019122520000601
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
날짜를 8자리로 입력하세요~!!! 예)2019122520000601
윤년입니다~!!!!
윤달입니다~!!!
이달은 30일 까지 있습니다.
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
날짜를 입력하세요~!!!5
토요일
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
날짜를 입력하세요~!!!7
일요일
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
2
5
7
7 5 2
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================10
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 35, in <module>
    n= int(input())
ValueError: invalid literal for int() with base 10: '================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================10'
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================10
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 35, in <module>
    n= int(input())
ValueError: invalid literal for int() with base 10: '================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================10'
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 35, in <module>
    n= int(input())
ValueError: invalid literal for int() with base 10: '================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py ================='
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================10
5
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================10 5
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================5
10
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 39, in <module>
    if(n%2==0):
TypeError: not all arguments converted during string formatting
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================10
50
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 39, in <module>
    if(n%2==0):
TypeError: not all arguments converted during string formatting
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
5
10
10
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================15
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 35, in <module>
    n= int(input())
ValueError: invalid literal for int() with base 10: '================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================15'
2
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
15
15
30
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 35, in <module>
    n= int(input())
ValueError: invalid literal for int() with base 10: '================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py ================='
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
20
21
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================-5
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 35, in <module>
    n= int(input())
ValueError: invalid literal for int() with base 10: '================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================-5'
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================-5
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 35, in <module>
    n= int(input())
ValueError: invalid literal for int() with base 10: '================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================-5'
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================

================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================5
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 35, in <module>
    n= int(input())
ValueError: invalid literal for int() with base 10: '================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================5'
>>> -5
-5
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================5
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 35, in <module>
    n= int(input())
ValueError: invalid literal for int() with base 10: '================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================5'
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
-5
5
>>> 5
5
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
용량은?(GB)2

1.byte
2.kbyte
3.Mbyte 선택 : 12
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
용량은?(GB)2

1.byte
2.kbyte
3.Mbyte
선택 : 12
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
용량은?(GB)2

1.byte
2.kbyte
3.Mbyte
선택 : 3
2048Mbyte
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
sfsd
아이디 입니다.
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================sdfsd
sdfsdf
아이디 입니다.
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================hello world
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 37, in <module>
    i = int(input())
ValueError: invalid literal for int() with base 10: '================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================hello world'
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
helloworld
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 37, in <module>
    i = int(input())
ValueError: invalid literal for int() with base 10: 'helloworld'
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
hello world
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day03/day03_out.py", line 37, in <module>
    i = int(input())
ValueError: invalid literal for int() with base 10: 'hello world'
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day03/day03_out.py =================
이름을 입력하세요~!!!홍길동
학번을 입력하세요20195478
78
95
67
홍길동 
 20195478 
 240 
 80.0 
B
>>> 
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
>>> 
