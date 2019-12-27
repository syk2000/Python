Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
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
>>> ㅣ[6:7]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    ㅣ[6:7]
NameError: name 'ᅵ' is not defined
>>> ㅣ[6:8]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ㅣ[6:8]
NameError: name 'ᅵ' is not defined
>>> ㅣ[6:7]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ㅣ[6:7]
NameError: name 'ᅵ' is not defined
>>> l
'Hello World'
>>> l[6:7]
'W'
>>> l[6:8]
'Wo'
>>> id(a),id(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    id(a),id(b)
NameError: name 'a' is not defined
>>> id(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    id(a)
NameError: name 'a' is not defined
>>> a=[1,2,3,4]
>>> b=[5,6,7,8]
>>> a+b
[1, 2, 3, 4, 5, 6, 7, 8]
>>> a*3
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> a.append()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.append()
TypeError: append() takes exactly one argument (0 given)
>>> a.append(5)
>>> a
[1, 2, 3, 4, 5]
>>> a.append(15)
>>> a
[1, 2, 3, 4, 5, 15]
>>> a.pop
<built-in method pop of list object at 0x000001BFECEE8808>
>>> a.pop()
15
>>> a
[1, 2, 3, 4, 5]
>>> b=[2,5,1,6,7,0]
>>> b.sort()
>>> b
[0, 1, 2, 5, 6, 7]
>>> b.reverse()
>>> b
[7, 6, 5, 2, 1, 0]
>>> b.index(6)
1
>>> c=[0,0,1,2,2,3]
>>> c
[0, 0, 1, 2, 2, 3]
>>> c.index(0)
0
>>> c.insert(4,9999)
>>> c
[0, 0, 1, 2, 9999, 2, 3]
>>> c.remove(2)
>>> c
[0, 0, 1, 9999, 2, 3]
>>> a+c
[1, 2, 3, 4, 5, 0, 0, 1, 9999, 2, 3]
>>> a.extend(c)
>>> a
[1, 2, 3, 4, 5, 0, 0, 1, 9999, 2, 3]
>>> c.count(00)
2
>>> del(c[3])
>>> c
[0, 0, 1, 2, 3]
>>> 
>>> len(a)
11
>>> range(0,3)
range(0, 3)
>>> a= ranger(0,30)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a= ranger(0,30)
NameError: name 'ranger' is not defined
>>> a=range
>>> a=range(0,3)
>>> a[0]
0
>>> a[1]
1
>>> a[2]
2
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a[3]
IndexError: range object index out of range
>>> print(a)
range(0, 3)
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
>>> for i in range(2,8,1)
SyntaxError: invalid syntax
>>> for i in range(2,8,1):
	print(i)

	
2
3
4
5
6
7
>>> for i in range(3,14,1):
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
>>> fori in range(4,20,3):
	
SyntaxError: invalid syntax
>>> for i in range(4,20,3):
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
>>> for i in range(1,11):
	sum+=i
	print(sum)

	
Traceback (most recent call last):
  File "<pyshell#79>", line 2, in <module>
    sum+=i
TypeError: unsupported operand type(s) for +=: 'builtin_function_or_method' and 'int'
>>> for i in range(1,11):
	int(sum)+=int(i)
	print(sum)
	
SyntaxError: can't assign to function call
>>> for i in range(1,11):
	int(res)+=int(i)
	
SyntaxError: can't assign to function call
>>> for i in range(1,11):
	int(res)+=int(i)
	
SyntaxError: can't assign to function call
>>> for i in range(1,11):
	print(int(i++))
	
SyntaxError: invalid syntax
>>> res=0
>>> for i in range(1,11):
	res= int(res)+int(i)
print(res)
SyntaxError: invalid syntax
>>> for i in range(1,11):
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
>>> res = 0
>>> for i in range(1,30):
	res+=int(i)
	if(i%5==0):
		print("\n")
	else:
		print("%s\t"%(i))

		
1	
2	
3	
4	


6	
7	
8	
9	


11	
12	
13	
14	


16	
17	
18	
19	


21	
22	
23	
24	


26	
27	
28	
29	
>>> for i in range(1,31):
	if(i%5==0):
		print("\n")
	else:
		print("%s\t"%(i),end="")

		
1	2	3	4	

6	7	8	9	

11	12	13	14	

16	17	18	19	

21	22	23	24	

26	27	28	29	

>>> for i in range(1,31):
	if(i%5==1):
		print("\n")
	else:
		print("%s\t"%(i),end="")

		


2	3	4	5	

7	8	9	10	

12	13	14	15	

17	18	19	20	

22	23	24	25	

27	28	29	30	
>>> for i in range(0,31):
	if(i%5==1):
		print("\n")
	else:
		print("%s\t"%(i),end="")

		
0	

2	3	4	5	

7	8	9	10	

12	13	14	15	

17	18	19	20	

22	23	24	25	

27	28	29	30	
>>> for i in range(0,31):
	if(i%5==0):
		print("%s\n"%(i))
	else:
		print("%s\t"%(i),end="")

		
0

1	2	3	4	5

6	7	8	9	10

11	12	13	14	15

16	17	18	19	20

21	22	23	24	25

26	27	28	29	30

>>> for i in range(1,31):
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

>>> st = "It is a fun Python class"
>>> res=0
>>> res1=0
>>> res2=0
>>> for i in st:
	if(i==a):
		res+=1
	elif(i==s):
		res1+=1

	
Traceback (most recent call last):
  File "<pyshell#128>", line 4, in <module>
    elif(i==s):
NameError: name 's' is not defined
>>> for i in st:
	res2+=1
	if(i==a):
		res+=1
	elif(i==s):
		res1+=1
print("a의 개수: %s \nb의 개수%s \n전체개수: %s\n"%(res,res1,res2))
SyntaxError: invalid syntax
>>> for i in st:
	res2+=1
	if(i==a):
		res+=1
	elif(i==s):
		res1+=1
	print("a의 개수: %s \nb의 개수%s \n전체개수: %s\n"%(res,res1,res2))

	
Traceback (most recent call last):
  File "<pyshell#133>", line 5, in <module>
    elif(i==s):
NameError: name 's' is not defined
>>> for i in st:
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
>>> for i in st:
	res2+=1
	if(i=='a'):
		res+=1
	elif(i=='s'):
		res1+=1
	print("a의 개수: %s \nb의 개수%s \n전체개수: %s\n"%(res,res1,res2))

a의 개수: 2 
b의 개수3 
전체개수: 26

a의 개수: 2 
b의 개수3 
전체개수: 27

a의 개수: 2 
b의 개수3 
전체개수: 28

a의 개수: 2 
b의 개수3 
전체개수: 29

a의 개수: 2 
b의 개수4 
전체개수: 30

a의 개수: 2 
b의 개수4 
전체개수: 31

a의 개수: 3 
b의 개수4 
전체개수: 32

a의 개수: 3 
b의 개수4 
전체개수: 33

a의 개수: 3 
b의 개수4 
전체개수: 34

a의 개수: 3 
b의 개수4 
전체개수: 35

a의 개수: 3 
b의 개수4 
전체개수: 36

a의 개수: 3 
b의 개수4 
전체개수: 37

a의 개수: 3 
b의 개수4 
전체개수: 38

a의 개수: 3 
b의 개수4 
전체개수: 39

a의 개수: 3 
b의 개수4 
전체개수: 40

a의 개수: 3 
b의 개수4 
전체개수: 41

a의 개수: 3 
b의 개수4 
전체개수: 42

a의 개수: 3 
b의 개수4 
전체개수: 43

a의 개수: 3 
b의 개수4 
전체개수: 44

a의 개수: 3 
b의 개수4 
전체개수: 45

a의 개수: 3 
b의 개수4 
전체개수: 46

a의 개수: 4 
b의 개수4 
전체개수: 47

a의 개수: 4 
b의 개수5 
전체개수: 48

a의 개수: 4 
b의 개수6 
전체개수: 49

>>> for i in st:
	res2+=1
	if(i=='a'):
		res+=1
	elif(i=='s'):
		res1+=1
print("a의 개수: %s \nb의 개수%s \n전체개수: %s\n"%(res,res1,res2))
SyntaxError: invalid syntax
>>> for i in st:
	res2+=1
	if(i=='a'):
		res+=1
	elif(i=='s'):
		res1+=1
		
print("a의 개수: %s \nb의 개수%s \n전체개수: %s\n"%(res,res1,res2))
SyntaxError: invalid syntax
>>> 
>>> print("a의 개수: %s \nb의 개수%s \n전체개수: %s\n"%(res,res1,res2))
a의 개수: 4 
b의 개수6 
전체개수: 49

>>> res=0
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

>>> ls = [10,5,20,7,9,31,12,11,19,32]
>>> for i in ls
SyntaxError: invalid syntax
>>> res =0;
>>> res=1
>>> for i in ls:
	if(i%2==0):
		res+=int(i)
		print("짝수 %s"%(res))
	elif(i%2==1):
		res1+=int(i)
		print("홀수 %s"%(res1))

		
짝수 11
홀수 8
짝수 31
홀수 15
홀수 24
홀수 55
짝수 43
홀수 66
홀수 85
짝수 75
>>> print("짝수 %s \n홀수 %s"%(res,res1))
짝수 75 
홀수 85
>>> res=0
>>> res1=0
>>> for ls in 10:
	if(ls%2==0):
		res+=int(ls)
		print("짝수 %s"%(res))
		res=0
	elif(ls%2==1):
		res1+=int(ls)
		print("홀수 %s"%(res1))
		res1=0

		
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    for ls in 10:
TypeError: 'int' object is not iterable
>>> for ls in 10:
	if(ls%2==0):
		res+=ls
		print("짝수 %s"%(res))
		res=0
	elif(ls%2==1):
		res1+=ls
		print("홀수 %s"%(res1))
		res1=0

		
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    for ls in 10:
TypeError: 'int' object is not iterable
>>> ls = [10,5,20,7,9,31,12,11,19,32]
>>> res=0
>>> res1=0
>>> res2=0
>>> for i in ls:
	ls(i)
	if(ls(i)%2==0)
	
SyntaxError: invalid syntax
>>> ls = [10,5,20,7,9,31,12,11,19,32]
>>> res=0
>>> res1=0
>>> res2=0
>>> for i in ls:
	ls(i)
	if(ls(i)%2==0):
		
SyntaxError: multiple statements found while compiling a single statement
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
>>> for i in ls:
	ls[i]
	if(ls[i]%2==0):
		res.append()
		print("짝수 %s"%(res))
	elif(ls[i]%2==1):
		print("홀수 %s"%(res))

		
Traceback (most recent call last):
  File "<pyshell#199>", line 2, in <module>
    ls[i]
IndexError: list index out of range
>>> 
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
>>> for i in range(0,len(ls),2):
	print("짝수번째",ls[i])
	print("홀수번째",ls[i-1])

	
짝수번째 10
홀수번째 32
짝수번째 20
홀수번째 5
짝수번째 9
홀수번째 7
짝수번째 12
홀수번째 31
짝수번째 19
홀수번째 11
>>> ls
[10, 5, 20, 7, 9, 31, 12, 11, 19, 32]
>>> for i in range(0,len(ls),2):
	print("짝수번째",ls[i-1])
	print("홀수번째",ls[i])

	
짝수번째 32
홀수번째 10
짝수번째 5
홀수번째 20
짝수번째 7
홀수번째 9
짝수번째 31
홀수번째 12
짝수번째 11
홀수번째 19
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
	ex01.append(ls[i])

	
짝수번째 5
홀수번째 10
Traceback (most recent call last):
  File "<pyshell#228>", line 4, in <module>
    ex.append(ls[i+1])
NameError: name 'ex' is not defined
>>> ex
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    ex
NameError: name 'ex' is not defined
>>> ex=[]
>>> ex1=[]
>>> for i in range(0,len(ls),2):
	print("짝수번째",ls[i+1])
	print("홀수번째",ls[i])
	ex.append(ls[i+1])
	ex01.append(ls[i])

	
짝수번째 5
홀수번째 10
Traceback (most recent call last):
  File "<pyshell#233>", line 5, in <module>
    ex01.append(ls[i])
NameError: name 'ex01' is not defined
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
>>> rx
Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    rx
NameError: name 'rx' is not defined
>>> ex
[5, 5, 7, 31, 11, 32]
>>> ex01
Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    ex01
NameError: name 'ex01' is not defined
>>> ex1
[10, 20, 9, 12, 19]
>>> l_ev
Traceback (most recent call last):
  File "<pyshell#241>", line 1, in <module>
    l_ev
NameError: name 'l_ev' is not defined
>>> l_ev=[]
>>> l_od=[]
>>> for i in ls:
	if(is_ev): lev_append(i)
	else: l_od.append(i)
	is_ev = not(is ev)
	
SyntaxError: invalid syntax
>>> for i in ls:
	if(is_ev): lev_append(i)
	else: l_od.append(i)
	is_ev = not(is_ev)

	
Traceback (most recent call last):
  File "<pyshell#249>", line 2, in <module>
    if(is_ev): lev_append(i)
NameError: name 'is_ev' is not defined
>>> clear
Traceback (most recent call last):
  File "<pyshell#250>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> for i in range(4):
	for i in range(7):
		print("*",end='')
	print("")

	
*******
*******
*******
*******
>>> for i in range(5):
	for i in range(1,5):
		print("*",end='')
	print("\n")

	
****

****

****

****

****

>>> for i in range(5):
	for i in range(1,6,1):
		print("*")
	print("\n")

	
*
*
*
*
*


*
*
*
*
*


*
*
*
*
*


*
*
*
*
*


*
*
*
*
*


>>> for i in range(0,5,1):
	for i in range(1,i<6,1):
		print("*")
	print("\n")

	










>>> for i in range(0,5,1):
	for i in range(1,6,1):
		print("*")
	print("\n")

	
*
*
*
*
*


*
*
*
*
*


*
*
*
*
*


*
*
*
*
*


*
*
*
*
*


>>> for i in range(0,5,1):
	for j in range(1,6,1):
		print("*")
	print("\n")

	
*
*
*
*
*


*
*
*
*
*


*
*
*
*
*


*
*
*
*
*


*
*
*
*
*


>>> for i in range(0,5,1):
	for j in range(i):
		print("*")
	print("\n")

	


*


*
*


*
*
*


*
*
*
*


>>> for i in range(0,5,1):
	for j in range(i,6):
		print("*")
	print("\n")

	
*
*
*
*
*
*


*
*
*
*
*


*
*
*
*


*
*
*


*
*


>>> for i in range(0,5,1):
	for j in range(i+1):
		print("*",end='')
	print("")

	
*
**
***
****
*****
>>> for i in range(0,5,1):
	for j in range(5,i-1,-1):
		print("*",end='')
	print("")

	
******
*****
****
***
**
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
	for j in range(5,i+1,1):
		print("*",end='')
	for s in range(4,4,-1)
		print(" ")
	print("")
	
SyntaxError: invalid syntax
>>> for i in range(0,5,1):
	for j in range(5,i+1,1):
		print("*",end='')
	for s in range(4,4,-1):
		print(" ")
	print("")

	





>>> for i in range(0,5,1):
	for j in range(5,i+1,1):
		print("*",end='')
	for s in range(4,j,-1):
		print(" ")
	print("")

	





>>> for i in range(0,5,1):
	for s in range(5,j,-1):
		print(" ")
	for j in range(5,i+1,1):
		print("*",end='')
	
	print("")

	





>>> j=0
>>> for i in range(0,5,1):
	for s in range(5,j,-1):
		print(" ")
	for j in range(5,i+1,1):
		print("*",end='')
	print("")

	
 
 
 
 
 

 
 
 
 
 

 
 
 
 
 

 
 
 
 
 

 
 
 
 
 

>>> for i in range(0,5,1):
	for s in range(5,j,-1):
		print(".")
	for j in range(5,i+1,1):
		print("*",end='')
	print("")

	
.
.
.
.
.

.
.
.
.
.

.
.
.
.
.

.
.
.
.
.

.
.
.
.
.

>>> for i in range(0,5,1):
	for s in range(5,j,-1):
		print(".",end='')
	for j in range(5,i+1,1):
		print("*",end='')
	print("")

	
.....
.....
.....
.....
.....
>>> for i in range(0,5,1):
	for j in range(5,i+1,1):
		print("*",end='')
	for s in range(5,j,-1):
		print(".",end='')
	print("")

	
.....
.....
.....
.....
.....
>>> for i in range(0,5,1):
	for j in range(5,i+1,1):
		print("*",end='')
	for s in range(5,j,-1):
		print(" ",end='')
	print("")

	
     
     
     
     
     
>>> for i in range(0,5,1):
	for j in range(0,i+1,1):
		print("*",end='')
	for s in range(5,j,-1):
		print(" ",end='')
	print("")

	
*     
**    
***   
****  
***** 
>>> for i in range(0,5,1):
	for s in range(5,j,-1):
		print(" ",end='')
	for j in range(0,i+1,1):
		print("*",end='')
	print("")

	
 *
     **
    ***
   ****
  *****
>>> for i in range(0,5,1):
	for s in range(5,j-1,-1):
		print(" ",end='')
	for j in range(0,i+1,1):
		print("*",end='')
	print("")

	
  *
      **
     ***
    ****
   *****
>>> for i in range(0,5,1):
	for s in range(5,j,-1):
		print(" ",end='')
	for j in range(0,i+1,1):
		print("*",end='')
	print("")

	
 *
     **
    ***
   ****
  *****
>>> for i in range(0,5,1):
	for s in range(5-i,j,-1):
		print(" ",end='')
	for j in range(0,i+1,1):
		print("*",end='')
	print("")

	
 *
    **
  ***
****
*****
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
>>> for i in range(0,3,1):
	for s in range(i):
		print(" ",end='')
	for j in range(1,i+2):
		print("*",end='')
	print("")

	
*
 **
  ***
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
	for s in range(3-i):
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
	for s in range(4-i):
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
	for s in range(1-i):
		print(" ",end='')
	for j in range(i+1):
		print("*",end='')
	print("")

	
 *
**
***
****
*****
>>> for i in range(5):
	if(i>3):
		for s in range(5//2-i):
		    print(" ",end='')
		for j in range(i*2+1):
		    print("*",end='')
	else:
		for j in range(i-5//2):
			print(" ",end='')
		for k in range(5-(i-5//2)*2)
		print("*",end='')
	print("")
	
SyntaxError: invalid syntax
>>> for i in range(5):
	if(i>3):
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
	
SyntaxError: expected an indented block
>>> for i in range(5):
	if(i>3):
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

	
*********
*******
*****
 ***
*********
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
>>> 
