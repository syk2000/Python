>>> st="python"
>>> st.center(10)
'  python  '
>>> st.center(2)
'python'
>>> st.ljust(10)
'python    '
>>> st.ljust(20)
'python              '
>>> st.ljust(3)
'python'
>>> st.rjust(10)
'    python'
>>> st.rjust(20)
'              python'
>>> st.center(20,'-')
'-------python-------'
>>> st.ljust(20,'-')
'python--------------'
>>> st.rjust(20,'-')
'--------------python'
>>> st.zfill(20)
'00000000000000python'


>>> "1234".isdigit()
True
>>> a="1234"
>>> a.isdigit()
True
>>> "abc".isalpha()
True
>>> a="abc"
>>> a.isalpha()
True
>>> a.isalnum()
True
>>> a="#"
>>> a.isalpha()
False
>>> a="abc12"
>>> a.isalnum()
True
>>> a.islower()
True
>>> a="ABC12"
>>> a.isupper()
True
>>> "12".islower()
False
>>> "    ".isspace()
True
>>> """

""".isspace()
True


>>> info="""
jo 9abc08-3022023
cho 900402=1011232
test 1234567-1234567
lee 980908-3a2b0c3
kim 900514-2022023
"""
>>> info.isspace()
False
>>> info.isalpha()
False
>>> info.isalnum()
False
>>> info.islower()
True
>>> info.isupper()
False

>>> t= info.splitlines()
>>> for i in t:
	inx = i.find('-')
	print(i[:inx],i[inx+1:])

	
 
jo 9abc08 3022023
cho 900402=101123 cho 900402=1011232
test 1234567 1234567
lee 980908 3a2b0c3
kim 900514 2022023


info="""
jo 9abc08-3022023
cho 900402=1011232
test 1234567-1234567
lee 980908-3a2b0c3
kim 900514-2022023
"""
t= info.splitlines()

for i in t:
	inx = i.find('-')
	print(i[:inx],i[inx+1:])
	print(i.replace(i[inx+1:],"******"))

================= RESTART: D:/평일_파이썬_신윤규/day10/day10_out.py =================
 
******
jo 9abc08 3022023
jo 9abc08-******
cho 900402=101123 cho 900402=1011232
******
test 1234567 1234567
test ******-******
lee 980908 3a2b0c3
lee 980908-******
kim 900514 2022023
kim 900514-******

#===============================================================================
info="""
jo 9abc08-3022023
cho 900402=1011232
test 1234567-1234567
lee 980908-3a2b0c3
kim 900514-2022023
"""
t= info.splitlines()

for i in t:
	inx=i.find('-')
	tmp=i.split()
	tmp=tmp[1].split('-')
	if(tmp[0].isdigit() and tmp[1].isdigit() and len(tmp[0])==6):
		print(i.replace(i[inx+1:],"********"))
	else:
		print(i)

#===============================================================================
>>> t='NeVer EvEr giVe up'
>>> t.title()
'Never Ever Give Up'
>>> T=t.title()
>>> T
'Never Ever Give Up'
>>> T.replace(' ','-')
'Never-Ever-Give-Up'

#===============================================================================
>>> def func(n,m,l):
	res = n+m+l
	return res

>>> a=func(1,2,3)
>>> a
6
>>> def test():
	print("")

	
>>> test()

>>> a=test()

>>> def test2():
	return

>>> test2()
>>> a=test2()
>>> print(a)
None
>>> def func(n=1,m=2,l=3):
	res = n+m+l
	return res

>>> func()
6
>>> func(2)
7
>>> func(l=10)
13
>>> lambda x,y: x+y
<function <lambda> at 0x000001B98C6EC1E0>
>>> (lambda x,y: x+y)(1,2)
3
>> y
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> y=10
>>> (lambda x:x+y)(10)
20
>>> (lambda x:y = x)(10)
SyntaxError: invalid syntax


>>> def func(n):
	return n+10
    
>>> ls=[1,2,3,4]
>>> map(func,ls)
<map object at 0x000001B98D0A5EB8>
>>> list((lambda x: x+10, ls))
[<function <lambda> at 0x000001B98D0B6AE8>, [1, 2, 3, 4]]

>>> a= input()
1 2 3 4 5
>>> a= a.split()
>>> a
['1', '2', '3', '4', '5']
>>> a= list(map(int, a))
>>> a
[1, 2, 3, 4, 5]
>>> a= list(map(int, input().split()))

>>> a
[]

>>> a=input()
1 2 3 4 5
>>> a= list(filter(lambda x: True, ls))
>>> list(filter(lambda x: x%2==0,ls))
[2, 4]

>>> from functools import reduce
>>> reduce(lambda x,y: x+y,[1,2,3,4,5])
15
>>> reduce(lambda x,y: x+1, [1,2,3,4,5])
5
>>> reduce(lambda x,y: y+1, [1,2,3,4,5])
6
>>> reduce(lambda x,y: x*y, [1,2,3,4,5])
120
>>> reduce(lambda x,y: x/y, [1,2,3,4,5])
0.008333333333333333

>>> a=4
>>> b=8
>>> add = lambda x,y: x+y
>>> add(4,8)
12

>>> lambda x:4 if x==1 else 0
<function <lambda> at 0x000001B98D0F7D90>
>>> a= lambda x:4 if x==1 else 0
>>> a(1)
4
>>> a(4)
0

>>> test = lambda x:print("hello") if x==1 else print("world")
>>> test(2)
world
>>> test(1)
hello


>>> sorted
<built-in function sorted>
>>> a=[2,3,5,65]
>>> a
[2, 3, 5, 65]
>>> sorted(a)
[2, 3, 5, 65]
>>> a={1:2,2:5,0:1}
>>> a
{1: 2, 2: 5, 0: 1}
>>> sorted(a)
[0, 1, 2]
>>> sorted(a,key=lambda x:a[x])
[0, 1, 2]
>>> b=[("gildong",1),("kwangsu",0)]
>>> sorted(b)
[('gildong', 1), ('kwangsu', 0)]
>>> sorted(b,key=lambda x: x[1])
[('kwangsu', 0), ('gildong', 1)]
>>> stu = [("dave",'8',10),("jane",'8',12)]
>>> sorted(stu)
[('dave', '8', 10), ('jane', '8', 12)]
