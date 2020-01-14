"""
num1 = int(input("뭐라고 출력할지1"))
num2 = int(input("뭐라고 출력할지2"))
#num1 와 num2 를 input 으로
#입력받아보세요
if(num1 > num2):
    print("num1 is larger than num2")
else:
    print("num2 is larger than num1")
"""
'''
숫자를 입력 받아서, 짝수인지 아닌지
출력하세요
(2로 나눠 나머지가 1이면 홀수)
'''
"""
num = int(input())
if(num % 2 == 0):
    print("is not odd")
#print("...") #<-이러면 안됨
else:
    print("is odd")
"""

#두 숫자를 입력받아(input)
#둘 중 어느 숫자가 더 큰지,
#같다면, 같음을 출력하세요

"""
n1= int(input())
n2= int(input())

if(n1 > n2):
    print("n1 is larger")
elif(n2>n1):
    print("n2 is larger")
else:
    print("same same e da")
"""

date = int(input())
#yyyymmdd
year = date // 10000
m = (date // 100) % 100

#print(year)
#print(m)

#윤년인지 여부
#이번달이 몇일 까지 인지(30,31,29,28)
#state = False
#아래 코드를
#if문 안에 if문을 넣는 형식으로
#바꿔봅시다
if(year % 400 == 0):
    state = True
elif(year % 4 == 0 and year % 100 == 0):
    state = False
elif(year % 4 == 0):
    state = True
else:
    state = False
print("%d년은 "%(year), end='')
if(state):
    print("윤년 입니다.")
else:
    print("평년 입니다.")

if(year % 4 ==0):
    if(year % 100 == 0):
        if(year % 400 ==0):
            state2 = True
        else:
            state2 = False
    else:
        state2=True
else:
    state2 = False
    
print("%d년은 "%(year), end='')
if(state2):
    print("윤년 입니다.")
else:
    print("평년 입니다.")




if(m == 1 or m==3 or m==5 or m==7 or m==10 or m==12):
    end_d = 31
elif(m==2):
    if(state):
        end_d = 29
    else:
        end_d = 28
else:
    end_d = 30
print("%d월은 %d일 까지 있습니다"%(m,end_d))


