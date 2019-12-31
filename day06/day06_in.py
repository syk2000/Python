Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a={
	[1,2,3],
	[4,5,6],
	[7,8,9]
	}
Traceback (most recent call last):
  File "<pyshell#0>", line 4, in <module>
    [7,8,9]
TypeError: unhashable type: 'list'
>>> a
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=[]
>>> a=[]
>>> a
[]
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day06/day_ex.py", line 3, in <module>
    [4,5,6]
TypeError: list indices must be integers or slices, not tuple
>>> a
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
>>> a
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> a[0]
[1, 2, 3]
>>> a[0][0]
1
>>> for i in range(3):
	for j input range(3):
		
SyntaxError: invalid syntax
>>> for in in range(3):
	
SyntaxError: invalid syntax
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
>>> ㅊ[2:-5]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    ㅊ[2:-5]
NameError: name 'ᄎ' is not defined
>>> c[2:-5]
[3, 4]
>>> c[-7:8]
[3, 4, 5, 6, 7, 8]
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
['이름']
['나이']
['주소']
['지울값']
['연봉']
['홍길동']
['20살']
['산골지기']
['지우세요']
['5000']
['김개똥']
['30살']
['지구촌']
['지우세요']
['4500']
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
 
['홍길동']
 
['20살']
 
['산골지기']
 
['지우세요']
 
['5000']
 
['김개똥']
 
['30살']
 
['지구촌']
 
['지우세요']
 
['4500']
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
 
  ['홍길동']
 
  ['20살']
 
  ['산골지기']
 
  ['지우세요']
 
  ['5000']
 
['김개똥']
 
['30살']
 
['지구촌']
 
['지우세요']
 
['4500']
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
 
%2s ['홍길동']
 
%2s ['20살']
 
%2s ['산골지기']
 
%2s ['지우세요']
 
%2s ['5000']
 
['김개똥']
 
['30살']
 
['지구촌']
 
['지우세요']
 
['4500']
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
 
['홍길동']
 
['20살']
 
['산골지기']
 
['지우세요']
 
['5000']
 
['김개똥']
 
['30살']
 
['지구촌']
 
['지우세요']
 
['4500']
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================


Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day06/day_ex.py", line 11, in <module>
    print(a[i][j])
NameError: name 'a' is not defined
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================


Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day06/day_ex.py", line 11, in <module>
    print(a[i][j])
NameError: name 'a' is not defined
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================


['이름']


['나이']


['주소']


['지울값']


['연봉']


['김개똥']


['30살']


['지구촌']


['지우세요']


['4500']
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
['이름']['나이']['주소']['연봉']
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day06/day_ex.py", line 9, in <module>
    ls[i][-1][0] = str(int(int(ls[i][3])*1.1))
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
['이름']['나이']['주소']['연봉']
['홍길동']['20살']['산골지기']['5500']
['김개똥']['30살']['지구촌']['4950']
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
>>> c=(1)
>>> c
1
>>> type(c)
<class 'int'>
>>> 
>>> d=(1,)
>>> d
(1,)
>>> type(d)
<class 'tuple'>
>>> ㄷ=1,
>>> ㄷ
(1,)
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
(1, 2, 3, 3, 3, 3)
>>> a=1,2,3,4,5
>>> type(c)
<class 'tuple'>
>>> type(d)
<class 'tuple'>
>>> q,w,e,r=a
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    q,w,e,r=a
ValueError: too many values to unpack (expected 4)
>>> q
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    q
NameError: name 'q' is not defined
>>> w
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    w
NameError: name 'w' is not defined
>>> e
(1,)
>>> r
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    r
NameError: name 'r' is not defined
>>> a=1,2,3,4
>>> q,w,e,r=a
>>> q
1
>>> w
2
>>> e
3
>>> r
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
>>> ㅁ
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
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
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
회사정보 	 :삼성전자
제품명 	 :갤럭시
가격정보 	 :100원
출시일 	 :미정
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
회사정보       :삼성전자
제품명       :갤럭시
가격정보       :100원
출시일       :미정
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
회사정보       :삼성전자
제품명       :갤럭시
가격정보       :100원
출시일       :미정
>>> def test():
	print("Hello world~!!!")

	
>>> test()
Hello world~!!!
>>> test(3)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    test(3)
TypeError: test() takes 0 positional arguments but 1 was given
>>> def test(n):
	print("Hello wolrd")

	
>>> n=3
>>> test(3)
Hello wolrd
>>> for n in range(5):
	test(n)

	
Hello wolrd
Hello wolrd
Hello wolrd
Hello wolrd
Hello wolrd
>>> test(235)
Hello wolrd
>>> def test2(num):
	print(num)

	
>>> test2(230)
230
>>> def ex(3)
SyntaxError: invalid syntax
>>> ex = int(input())
ex = int(input())
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    ex = int(input())
ValueError: invalid literal for int() with base 10: 'ex = int(input())'
>>> def test(a,b,c):
	print(a+b+c)

	
>>> test(1,2,3)
6
>>> 6
6
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
>>> test(2,3,4)
9
>>> test1(2,9,7)
18
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
6
!!! 15 !!!
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day06/day_ex.py", line 11, in <module>
    print("!!!",test2(4,5,6),"!!!")
NameError: name 'test2' is not defined
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
6
!!! 15 !!!
!!! 15 !!!
>>> a=5
>>> def test()
SyntaxError: invalid syntax
>>> 5
5
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
	global t
	t[2] = 4

	
>>> t
[1, 2, 999, 3]
>>> test_l3()
>>> t
[1, 2, 4, 3]
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
1. 학생등록
          2.학생 점수 등록
          3.학생 정보출력
          4.학생순위순 표기
          5.종료

=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
1. 학생등록
2.학생 점수 등록
3.학생 정보출력
4.학생순위순 표기
5.종료
1
학생의 이름을 등록하세요~!!!홍길
학생의 나이를 입력하세요~!!!56
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day06/day_ex.py", line 21, in <module>
    sel_1()
TypeError: sel_1() missing 2 required positional arguments: 'name' and 'age'
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
1. 학생등록
2.학생 점수 등록
3.학생 정보출력
4.학생순위순 표기
5.종료
1
학생의 이름을 등록하세요~!!!홀길
학생의 나이를 입력하세요~!!!25
1. 학생등록
2.학생 점수 등록
3.학생 정보출력
4.학생순위순 표기
5.종료
2
점수를 등록하세요~!!!95
1. 학생등록
2.학생 점수 등록
3.학생 정보출력
4.학생순위순 표기
5.종료
3
확인하고자 하는 학생 번호 입력:2
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day06/day_ex.py", line 26, in <module>
    print("%s번 학생 | 이름 : %s |나이: %s|점수: %s"%(n.stu_i[n][0],n.stu_i[n][1],n.stu_i[n][2]))
AttributeError: 'int' object has no attribute 'stu_i'
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
30
33
36
39
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day06/day_ex.py", line 42, in <module>
    print(func(10+i,10+i,10+i))
NameError: name 'func' is not defined
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day06/day_ex.py", line 42, in <module>
    print(func(10+i,10+i,10+i))
NameError: name 'func' is not defined
>>> def test():
	print("dddd")

	
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
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    test2(k,m,l)
NameError: name 'test2' is not defined
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
>>> k,m = swap(k,m)
>>> k
2
>>> m
1
>>> type(swap(1,2))
<class 'tuple'>
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
False
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
True
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
>>> res(5)
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    res(5)
  File "D:/평일_파이썬_신윤규/day06/day_ex.py", line 2, in res
    if(res(5,5)%2==0):
TypeError: res() takes 1 positional argument but 2 were given
>>> if(res(5)):
	print("ddd")

	
Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    if(res(5)):
  File "D:/평일_파이썬_신윤규/day06/day_ex.py", line 2, in res
    if(res(5,5)%2==0):
TypeError: res() takes 1 positional argument but 2 were given
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
>>> if(res(5)):
	print("ddd")

	
Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    if(res(5)):
  File "D:/평일_파이썬_신윤규/day06/day_ex.py", line 2, in res
    if(res(5,5)%2==0):
TypeError: res() takes 1 positional argument but 2 were given
>>> 
=================== RESTART: D:/평일_파이썬_신윤규/day06/day_ex.py ===================
>>> if(res(5)):
	pirnt("ddd")

	
>>> 
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
>>>  def test(*v):
	res01=0
	for i in v:
		return res01+= v
	
SyntaxError: unexpected indent
>>> def test(*v):
	res01=0
	for i in v:
		return res01+= v
	
SyntaxError: invalid syntax
>>> def test(*v):
	res01=0
	for i in v:
		return res01=res01 + v
	
SyntaxError: invalid syntax
>>> def test(*v):
	res01=0
	for i in v:
		return res01==res01+v

	
>>> test(1,2,34,5,13,4)
Traceback (most recent call last):
  File "<pyshell#247>", line 1, in <module>
    test(1,2,34,5,13,4)
  File "<pyshell#246>", line 4, in test
    return res01==res01+v
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
>>> def test(*v):
	res01=0
	for i in v:
		return res01==int(res01)+int(v)

	
>>> test(1,2,34,5,13,4)
Traceback (most recent call last):
  File "<pyshell#250>", line 1, in <module>
    test(1,2,34,5,13,4)
  File "<pyshell#249>", line 4, in test
    return res01==int(res01)+int(v)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
>>> def test(*v):
	res01=0
	for i in range(v):
		return res01==res01+v

	
>>> def test(*v):
	res01=0
	for i in range(v):
		return res01==res01+v
	print(res01)

	
>>> def sum_m(*v):
	res01=0
	for i in v:
		res01=res01+v
		return res01

>>> 
>>> sum_m(1,3,5,7,9,10)
Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    sum_m(1,3,5,7,9,10)
  File "<pyshell#259>", line 4, in sum_m
    res01=res01+v
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
>>> def sum_m(*v):
	res01=0
	for i in v:
		res01=int(res01)+int(v)
		return res01

	
>>> sum_m(1,3,5,7,9,10)
Traceback (most recent call last):
  File "<pyshell#264>", line 1, in <module>
    sum_m(1,3,5,7,9,10)
  File "<pyshell#263>", line 4, in sum_m
    res01=int(res01)+int(v)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
>>> sum_m([1,3,5,7,9,10])
Traceback (most recent call last):
  File "<pyshell#265>", line 1, in <module>
    sum_m([1,3,5,7,9,10])
  File "<pyshell#263>", line 4, in sum_m
    res01=int(res01)+int(v)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
>>> 
