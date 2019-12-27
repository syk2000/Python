>>> List = [3,4,7,9]
>>> List[3]
9

>>> List[:2]
[3, 4]

>>> List[1:2]
[4]
>>> "Hello world"
'Hello world'
>>> l = "Hello World"
>>> l
'Hello World'
>>> l[6:]
'World'
#Wo만 잘라내 보자
>>> l[6:8]
'Wo'
>>> a=[1,2,3,4]
>>> b=[5,6,7,8]
>>> a+b
[1, 2, 3, 4, 5, 6, 7, 8]
>>> a*3
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> a.append(5)
>>> a
[1, 2, 3, 4, 5]
>>> a.append(15)
>>> a
[1, 2, 3, 4, 5, 15]
>>> a.pop()
15
>>> a
[1, 2, 3, 4, 5]
>>> a
[1, 2, 3, 4, 5]
>>> b=[2,5,1,6,7,0]
>>> b.sort()
>>> b
[0, 1, 2, 5, 6, 7] #순차적으로 나타냄

>>> b.reverse()
>>> b
[7, 6, 5, 2, 1, 0] # 역순으로 나타냄

#특정 값 인덱스가 나온다.
>>> b.index(6)

#여러개의 값이 있을경우 제일 앞에 있는 것을 나오게 한다.
>>> c=[0,0,1,2,2,3]
>>> c
[0, 0, 1, 2, 2, 3]
>>> c.index(0)

>>> c.insert(4,9999)
>>> c
[0, 0, 1, 2, 9999, 2, 3]

#같은 수가 있으면 앞에 것이 삭제가 된다.
>>> c.remove(2)
>>> c

#a와 c가 따로 존재
>>> a+c
[1, 2, 3, 4, 5, 0, 0, 1, 9999, 2, 3]

#a값이 변하고 c값은 변동이 없
>>> a.extend(c)
>>> a
[1, 2, 3, 4, 5, 0, 0, 1, 9999, 2, 3]


>>> c.count(00)
2

>>> del(c[3])
>>> c
[0, 0, 1, 2, 3]

# 1부터 센다.
>>> len(a)
11


>>> a=range(0,3)
>>> a[0]
0
>>> a[1]
1
>>> a[2]
2
>>> print(a)
range(0, 3)

# 값을 바꿀 수가 없다.
>>> a[0]=2
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a[0]=2
TypeError: 'range' object does not support item assignment

>>> for i in range(4):
	print(i)

	
0
1
2
3

>>> for i in range(2,8,1):
	print(i)

	
2
3
4
5
6
7

#for문과 range를 사용하여 3부터 13까지 출력하자
>>> for i in range(3,14):
	print(i)

	
3
4
5
6
7
8
9
10
11
12
13

#for문과 range를 사용하여,4부터 20까지 3씩 건너뛰며 출력해보기
>>> for i in range(4,21,3):
	print(i)

	
4
7
10
13
16
19


>>> for i in range(10,-1,-1):
	print(i)

	
10
9
8
7
6
5
4
3
2
1
0

>>> res=0
>>>for i in range(1,11):
	res= int(res)+int(i)
	print(res)

	
1
3
6
10
15
21
28
36
45
55
>>> res
55

>>>for i in range(1,31):
	if(i%5==0):
		print("%s\n"%(i))
	else:
		print("%s\t"%(i),end="")

		
1	2	3	4	5

6	7	8	9	10

11	12	13	14	15

16	17	18	19	20

21	22	23	24	25

26	27	28	29	30

#=============================================================================
for i in st:
	res2+=1
	if(i=='a'):
		res+=1
	elif(i=='s'):
		res1+=1
	print("a의 개수: %s \nb의 개수%s \n전체개수: %s\n"%(res,res1,res2))

	
a의 개수: 0 
b의 개수0 
전체개수: 2

a의 개수: 0 
b의 개수0 
전체개수: 3

a의 개수: 0 
b의 개수0 
전체개수: 4

a의 개수: 0 
b의 개수0 
전체개수: 5

a의 개수: 0 
b의 개수1 
전체개수: 6

a의 개수: 0 
b의 개수1 
전체개수: 7

a의 개수: 1 
b의 개수1 
전체개수: 8

a의 개수: 1 
b의 개수1 
전체개수: 9

a의 개수: 1 
b의 개수1 
전체개수: 10

a의 개수: 1 
b의 개수1 
전체개수: 11

a의 개수: 1 
b의 개수1 
전체개수: 12

a의 개수: 1 
b의 개수1 
전체개수: 13

a의 개수: 1 
b의 개수1 
전체개수: 14

a의 개수: 1 
b의 개수1 
전체개수: 15

a의 개수: 1 
b의 개수1 
전체개수: 16

a의 개수: 1 
b의 개수1 
전체개수: 17

a의 개수: 1 
b의 개수1 
전체개수: 18

a의 개수: 1 
b의 개수1 
전체개수: 19

a의 개수: 1 
b의 개수1 
전체개수: 20

a의 개수: 1 
b의 개수1 
전체개수: 21

a의 개수: 1 
b의 개수1 
전체개수: 22

a의 개수: 2 
b의 개수1 
전체개수: 23

a의 개수: 2 
b의 개수2 
전체개수: 24

a의 개수: 2 
b의 개수3 
전체개수: 25

>>> res
2
>>> res1
3
>>> res2
25

#============================================================================
res=0
>>> res1=0
>>> res2=0
>>> for i in st:
	res2+=1
	if(i=='a'):
		res+=1
	elif(i=='s'):
		res1+=1

>>> print("a의 개수: %s \nb의 개수%s \n전체개수: %s\n"%(res,res1,res2))
a의 개수: 2 
b의 개수3 
전체개수: 24

#c,Java와는 다르게 따로 선언해 줘야 한다.


>>> num=[]
>>> num1=[]
>>> for i in range(0,len(ls),2):
	print(i)

	
0
2
4
6
8

>>> for i in range(1,len(ls),2)
SyntaxError: invalid syntax
>>> for i in range(1,len(ls),2):
	print(i)

	
1
3
5
7
9

>>> ls
[10, 5, 20, 7, 9, 31, 12, 11, 19, 32]
>>> for i in range(0,len(ls),2):
	print("짝수번째",ls[i+1])
	print("홀수번째",ls[i])

짝수번째 5
홀수번째 10
짝수번째 7
홀수번째 20
짝수번째 31
홀수번째 9
짝수번째 11
홀수번째 12
짝수번째 32
홀수번째 19


>>> for i in range(0,len(ls),2):
	print("짝수번째",ls[i+1])
	print("홀수번째",ls[i])
	ex.append(ls[i+1])
	ex1.append(ls[i])

	
짝수번째 5
홀수번째 10
짝수번째 7
홀수번째 20
짝수번째 31
홀수번째 9
짝수번째 11
홀수번째 12
짝수번째 32
홀수번째 19

>>> ex
[5, 5, 7, 31, 11, 32]


>>> ex1
[10, 20, 9, 12, 19]

>>> for i in range(4):
	for i in range(7):
		print("*",end='')
	print("")

	
*******
*******
*******
*******

>>> for i in range(0,5,1):
	for j in range(i+1):
		print("*",end='')
	print("")

	
*
**
***
****
*****

#===============================================================================
>>> for i in range(0,5,1):
	for j in range(5,i,-1):
		print("*",end='')
	print("")

	
*****
****
***
**
*


>>> for i in range(0,5,1):
	for s in range(5-i):
		print(" ",end='')
	for j in range(i+1):
		print("*",end='')
	print("")

	
     *
    **
   ***
  ****
 *****

>>> for i in range(0,5,1):
	for s in range(i):
		print(" ",end='')
	for j in range(5-i):
		print("*",end='')
	print("")

	
*****
 ****
  ***
   **
    *

>>> for i in range(5):
	if(i<3):
		for s in range(5//2-i):
		    print(" ",end='')
		for j in range(i*2+1):
		    print("*",end='')
	else:
		for j in range(i-5//2):
			print(" ",end='')
		for k in range(5-(i-5//2)*2):
			print("*",end='')
	print("")

	
  *
 ***
*****
 ***
  *






















