a = int(input("1st num"))
b = int(input("2nd num"))
c = int(input("3rd num"))

if(a%3==0):
    print(a)

if(a<0):
    a = a*-1

print(a)

if(a%2 != 0):
    print("is odd")
else:
    print("is not odd")

if(a<b):
    print(b)
else:
    print(a)

if(a<b):
    if(b<c):
        print(c)
    else:
        print(b)
else:
    if(a<c):
        print(c)
    else:
        print(a)


if(a<b):
    if(b%2 ==0):
        print(b)
else:
    if(a%2 == 0):
        print(a)

if(a<b):
    tmp = b
else:
    tmp = a

if(tmp % 2 == 0):
    print(tmp)

#=========================

tmp = a+b

if((a+b)%2==0):
    if((a+b)%3==0):
        print(a+b)

if(tmp%2 ==0 and tmp%3==0):
    print(tmp)







    








