
'''
date = input("날짜를 8자리로 입력하세요~!!! 예)20191225")
year = int(date) //10000
m = (int(date)//100)%100


if(year%400==0):
    state =True
elif(year % 4 ==0 and year %100==0):
    state = False
elif(year%4==0):
    state =True
else:
    state = False
print("%d년은 "%(year), end='')
if(state):
    print("윤년입니다.")
else:
    print("평년입니다.")

if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    end_d = 31
elif(m==2):
    if(state):
        end_d=29
    else:
        end_d=28
else:
    end_d=30


print()
'''


List = [1,2,3,4]
i = int(input())
if(i in List):
    print("yes")
else:
    print("no")

