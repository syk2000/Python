#===================================다중 상속======================================

>>> class A:
	def pa(self):
		print("A")

		
>>> class B:
	def pb(self):
		print("B")

		
>>> class C(A,B):
	pass

>>> c=C()
>>> c.pa()
A
>>> c.pb()
B
>>> class C(A,B):
	def pb(self):
		B.pb(self)

		
>>> c=C()
>>> c.pb
<bound method C.pb of <__main__.C object at 0x035F20B8>>
>>> c.pb()
B
>>> class A:
	def p(self):
		print("A")
	def pp(self):
		self.p()
	def ppp(self):
		self.__p()
	__p=p

	
>>> class B(A):
	def p(self):
		print("B")

		
>>> b=B()
>>> b.p()
B
>>> b.ppp()
A
>>> class A:
	def __p(self):
		print("A")
	def pp(self):
		self.__p()

		
>>> a=A()
>>> a.pp()
A

#------------------------------------------------------------------------------
class Person:
    info_form="""name:%s
age:%s
"""
    def __init__(self,name):
        self.n = name
    def p_name(self):
        return self.n
    def person_info(self):
        print(info_form%(self.p_name(),40))

class employ(Person):
    def init__(self,name,part):
        super().__init__(name)
        self.part=part

        def p_name(self):
            return self.part+":"+n
        
#==============================이터레이터=============================================
>>> class A:
	pass

>>> test = A()
>>> test.val=54
>>> test.name="dd"
>>> test.val
54
>>> test.name
'dd'
>>> s="abc"
>>> it = iter(s)
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    next(it)
StopIteration

#===============================================================================
class test:
    def __init__(self,data,n):
        self.d=data
        self.i=n

    def __iter__(self):
        #__next__ 메서드를 가진 객체 호출
        return self

    def __next__(self):
        #매 반복마다 출력을 정의,끝까지 가면, StopIteration 에러 raise
        if(self.i>0):
            self.i -=1
            return self.d
        else:
            raise StopIteration

#-------------------------------------------------------------------------------
=================== RESTART: D:/평일_파이썬_신윤규/day15/day13_out.py ==================
>>> t=test("hello",5)
>>> for i in t:
	print(i)

	
hello
hello
hello
hello
hello

#================================================================================
class test:
    def __init__(self,data,n):
        self.d=data
        self.i=n

    def __iter__(self):
        #__next__ 메서드를 가진 객체 호출
        return self

    def __next__(self):
        #매 반복마다 출력을 정의,끝까지 가면, StopIteration 에러 raise
        if(self.i>0):
            self.i -=1
            return self.d
        else:
            raise StopIteration

class myrange:
    def __init__(self,start, end, jump=1):
        self.s= start
        self.e=end
        self.j=jump

    def __iter__(self):
        return self

    def __next__(self):
        if(self.s>=self.e):
            raise StopIteration
        else:
            tmp=self.s
            self.s+=self.j
            return tmp

=================== RESTART: D:/평일_파이썬_신윤규/day15/day13_out.py ==================
>>> for i in myrange(1,9,2):
	print(i)

	
1
3
5
7
>>> for i in zip(range(3,17,3), myrange(3,17,3)):
	print(i)

	
(3, 3)
(6, 6)
(9, 9)
(12, 12)
(15, 15)

>>> [i*i for i in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> [(x,y) for x in range(1,10,1) for y in range(10,1,-1)]
[(1, 10), (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (2, 10), (2, 9), (2, 8), (2, 7), (2, 6), (2, 5), (2, 4), (2, 3), (2, 2), (3, 10), (3, 9), (3, 8), (3, 7), (3, 6), (3, 5), (3, 4), (3, 3), (3, 2), (4, 10), (4, 9), (4, 8), (4, 7), (4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (5, 10), (5, 9), (5, 8), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (6, 5), (6, 4), (6, 3), (6, 2), (7, 10), (7, 9), (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (8, 10), (8, 9), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4), (8, 3), (8, 2), (9, 10), (9, 9), (9, 8), (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2)]


>>> [(x,y) for x in range(1,10,1) for y in range(10,1,-1) if x>5 if y>5]
[(6, 10), (6, 9), (6, 8), (6, 7), (6, 6), (7, 10), (7, 9), (7, 8), (7, 7), (7, 6), (8, 10), (8, 9), (8, 8), (8, 7), (8, 6), (9, 10), (9, 9), (9, 8), (9, 7), (9, 6)]

>>> {x:0 for x in range(10)}
{0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
>>> [0 if x<5 else x for x in range(10)]
[0, 0, 0, 0, 0, 5, 6, 7, 8, 9]
>>> {"a":90,"b":70,"c":20}
{'a': 90, 'b': 70, 'c': 20}

>>> for i in (i*i for i in range(10)):
	print(i)

	
0
1
4
9
16
25
36
49
64
81

>>> a={1,2,3,4}
>>> b={4,5,6}
>>> a-b
{1, 2, 3}
>>> a+b
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> a.union(b)
{1, 2, 3, 4, 5, 6}






