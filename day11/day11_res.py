#예외 처리

try:
    sadfj
except:
    pass
print("pp")

================= RESTART: D:/평일_파이썬_신윤규/day11/day11_out.py =================
pp
>>>

#===============================================================================

try:
    sadfj
    print("cc")
except:
    pass
print("pp")

================= RESTART: D:/평일_파이썬_신윤규/day11/day11_out.py =================
pp

#===============================================================================
try:
    sadfj
    print("cc")
except NameError as e:
    print(e)
    pass
except Exception as e:
    print(e)
else:
    print("no_err")
print("pp")
================= RESTART: D:/평일_파이썬_신윤규/day11/day11_out.py =================
name 'sadfj' is not defined
pp

#================================================================================
try:
    5/0
    #sadfj
    print("cc")
except NameError as e:
    print(e)
    pass
except Exception as e:
    print(e)
else:
    print("no_err")
print("pp")

================= RESTART: D:/평일_파이썬_신윤규/day11/day11_out.py =================
division by zero
pp

#===============================================================================
a=input()
b=input()

if(a.isdigit() and b.isdigit()):
    print(int(a)+int(b))
else:
    print("숫자가 아니네")

try:
    print(int(a)+int(b))
except Exception as e:
    print("숫자가 아니네요")
    print(e)
================= RESTART: D:/평일_파이썬_신윤규/day11/day11_out.py =================
십
이
숫자가 아니네
숫자가 아니네요
inval

invalid literal for int() with base 10:
'================= RESTART: D:/평일_파이썬_신윤규/day11/day11_out.py =================tl'
================= RESTART: D:/평일_파이썬_신윤규/day11/day11_out.py =================
2
5
7
7

#===============================================================================
a=input()
b=input()

try:
    a=int(a)
    b=int(b)
    c= a/b
    
except ValueError as e:
    c=str(e)+"value_Err"
except ZeroDivisionError as e:
    c=str(e)+"0으로 나눈 에러"
except Exception as e:
    c=e

================= RESTART: D:/평일_파이썬_신윤규/day11/day11_out.py =================십
이
invalid literal for int() with base 10: '================= RESTART: D:/평일_파이썬_신윤규/day11/day11_out.py =================십'value_Err
>>> 
================= RESTART: D:/평일_파이썬_신윤규/day11/day11_out.py =================
1
2
0.5

#===============================================================================
'''
def func(a,b,c):
    a= input()
    b= input()
    c=int(a)+int(b)

    if((a==str and b==str) or(a==int and b==str) or (a==str and b==int)):
        print("오류")
    else:
        print(c)

'''

'''
try:
    a= input()
    b= input()
    c=int(a)+int(b)

    
except Exception as e:
    if((a==str and b==str) or(a==int and b==str) or (a==str and b==int)):
        print("오류")
    print(e)
    pass
else:
    print("오류가 아닙니다.")
    print(c)
    
'''
#===============================================================================
arr=[100,200]

try:
    print(arr[0]);print(arr[1]);print(arr[2])
    
except IndexError as e:
    print("index 벗어났스빈다. arr[2]")
    print(e)
    
i=100;j=0
print("나누기 진행 i/j",i/j)

================= RESTART: D:/평일_파이썬_신윤규/day11/day11_out.py =================
100
200
index 벗어났스빈다. arr[2]
list index out of range
Traceback (most recent call last):
  File "D:/평일_파이썬_신윤규/day11/day11_out.py", line 11, in <module>
    print("나누기 진행 i/j",i/j)
ZeroDivisionError: division by zero

#===============================================================================
arr=[100,200]

try:
    print(arr[0]);print(arr[1]);print(arr[2])
    
except IndexError as e:
    print("index 벗어났스빈다. arr[2]")
    print(e)

except ZeroDivisionError as e:
    i=100;j=0
    print("나누기 진행 i/j",i/j)
================= RESTART: D:/평일_파이썬_신윤규/day11/day11_out.py =================
100
200
index 벗어났스빈다. arr[2]
list index out of range

#===============================================================================
def sq(a):
    try:
        a= int(a)
        print(a*a)
    except Exception as e:
        print(e)
        return None
    else:
        print("문제 없이 수행")
    finally:
        print("끝")
    print("try 밖")
    return a*a

#===============================================================================
try:
    age = int(input("당신의 나이를 알려주세요~!!!"))
    if age<1:
	    raise Exception("age must be larger than 0")
except ValueError as e:
    print(e)
    print("숫자로 입력하세요~!!!")
except Exception as e:
    print(e)
    print("0살 이하의 나이는 없습니다.")

else:
    print("당신의 나이는 %d살 이군요~!!!"%(age))
finally:
    print("종료합니다.")

================= RESTART: D:/평일_파이썬_신윤규/day11/day11_out.py =================
당신의 나이를 알려주세요~!!!
invalid literal for int() with base 10: ''
숫자로 입력하세요~!!!
종료합니다.

#===============================================================================
ex,name = input("주민번호 앞자리와 이름").split()
try:
    if(len(ex) !=6):
        raise Exception("잘못 입력")

    if(not(ex.isdigit())):
        raise Exception("숫자 입력")
    year=int(ex[:2])

    if(not((year<=99 and year>20)or year in [0,1])):
        raise Exception("가입이 불가능한 나이")
    
    print(ex,year,name)
    
except Exception as e:
    #try구문에 오류 있을 경우 수행
    print("가입이 실패한 이유는",e,"때문입니다.")
else:
    #try 구문에 오류 없을 경우 수행
    print("가입이 가능합니다.")
    print("가입을 축하합니다.")
finally:
    #무조건 수행
    print("가입 프로세스 완료.")
'''
try:
    print("================회원가입 프로그램=================")
    year = input("주민번호 앞자리를 입력해주세요(6자리로 기입)")

except ValueError as e:
    if (year>=020101):
        raise Exception("가입이 불가능 합니다.")

except Exception as e:
    print("가입이 실패한 이유는 바로",e,"입니다.")

else:
    print("가입이 가능합니다.")
    print("가입을 축하합니다.")
finally:
    print("가입 프로세스 완료.")
'''
================= RESTART: D:/평일_파이썬_신윤규/day11/day11_out.py =================
주민번호 앞자리와 이름 000601 고길동
000601 0 고길동
가입이 가능합니다.
가입을 축하합니다.
가입 프로세스 완료.

#===============================================================================











