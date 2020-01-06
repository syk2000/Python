>>> menu={}
>>> menu['제육'] = 4500
>>> menu['제육']
4500
>>> menu.keys()
dict_keys(['제육'])
>>> menu.values()
dict_values([4500])
>>> import random as fn
>>> fn.random()
0.10211351793794754
#1~10까지 나오는 비율 정리하기 
from random import randint

n=10000 #반복 함수
m=10 #리스트를 쓰면 필요함(randint 범위)
li = list(range(m)) #통계 저장할 변수

for i in range(m+1):
    li.append(0)

for i in range(n):
    tmp = randint(0,m) #randint 결과 저장
    li[tmp] += 1            #결과 통계 저장(dict, list)

#???                 #Optional 통계치 보기좋게 수정

for i in range(m+1):
    print(i,li[i]/n*100,"%")

#-------------------------------------------------------------------------------
dictionary 사용

#1~10까지 나오는 비율 정리하기 
from random import randint

n=10000 #반복 함수
li={}
m=9

for i in range(n):
    tmp = randint(0,m) #randint 결과 저장
    li[tmp] = li.setdefault(tmp,0) +1


for i in li.keys():
    print(i,li[i]/n*100,"%")

#===============================================================================
#슬라이싱 문자열, 튜플, dic 


>>> s="hello"
>>> s[2:3]
'l'
>>> len(s)
5
>>> ks="한글"
>>> len(ks)
2
>>> ks[ :2]
'한글'
>>> ss="have a nice day"
>>> s.title()
'Hello'
>>> ss.title()
'Have A Nice Day'
>>> s.upper()
'HELLO'
>>> ss.upper()
'HAVE A NICE DAY'
>>> ss.swapcase()
'HAVE A NICE DAY'
>>> s.swapcase().title()
'Hello'
>>> ss.swapcase().title()
'Have A Nice Day'

>>> ss = "Helo Python"
>>> ss.find("t")
7

st="It is a fun Python class"
cnt_a = cnt_s = cnt =0
for i in st:
    cnt+=1
    if i =='a':
        cnt_a+=1
    elif i == 's':
        cnt_s+=1

print("총 개수 :", cnt,
      "\na 개수:",cnt_a,
      "\ns 개수: ",cnt_s)

================= RESTART: D:/평일_파이썬_신윤규/day09/day09_out.py =================
총 개수 : 24 
a 개수: 2 
s 개수:  3

#===============================================================================
st = "Have a nice day Have a nice day Have a nice day"
cnt=0
ls=[]
while True:
    cnt=st.find("a",cnt+1)
    if(cnt==-1): # while 탈출 조건
        break
    else:
        ls.append(cnt)


print("a의 개수 : ",st.count('a'))
print("위치 :",ls)

================= RESTART: D:/평일_파이썬_신윤규/day09/day09_out.py =================
a의 개수 :  9
위치 : [1, 5, 13, 17, 21, 29, 33, 37, 45]

#==============================================================================
>>> st ="         파이썬"
>>> st.strip()
'파이썬'

>>> st ="파파파파파파파이선파파파파파"
>>> st.strip("파")
'이선'
>>> st.lstrip()
'파파파파파파파이선파파파파파'
>>> st.rstrip("파")
'파파파파파파파이선
>>> date = "2015/5/6"
>>> date.replace('/','-')
'2015-5-6'
>>> date
'2015/5/6'

>>> st="""
김개똥 -2017년 03월 24일
홍길동구리 -2015년 04월 02일
선우선녀 -2018 05월 14일
"""
>>> st.replace('-',':')
'\n김개똥 :2017년 03월 24일\n홍길동구리 :2015년 04월 02일\n선우선녀 :2018 05월 14일\n'


>>> i=0
>>> while(True):
	i = st.find(':',i+1)
	if(i== -1):
		break
	print('index',i)
	st=st.replace(st[i+1:i+5],"1999")

>>> a= input()
123 455
>>> a
'123 455'
>>> a.split()
['123', '455']
>>> b,c=a.split()
>>> b
'123'
>>> c
'455'

>>> a="가나다라"
>>> a.join("/")
'/'
>>> a
'가나다라'
>>> a="""가
나
다
라"""
>>> b = a.splitlines()
>>> b
['가', '나', '다', '라']
>>> '-'.join
<built-in method join of str object at 0x00000181E9F38C00>
>>> a
'가\n나\n다\n라'






>>> ins = input()
12 13 25 6 74 324
>>> ins
'12 13 25 6 74 324'
>>> print(type(str))
<class 'type'>
>>> list_str=ins.split()
>>> for i in list_str:
	print(i)

	
12
13
25
6
74
324

>>> for i in list_str:
	print(int(i))

	
12
13
25
6
74
324

l=0
for i in list_str:
	l.append(int(i))


