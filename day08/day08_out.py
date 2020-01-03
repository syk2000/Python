import random
ls=[]

#가위 바위 보 선택
def sel():
    r=0
    c=0
    p=0
    if(len(ls)<5):
        return random.randint(0,2)
    for i in ls:
        if(i==0):
            c+=1
        elif(i==1):
            r+=1
        elif(i==2):
            p+=1

    if(c>r):
        if(c>p):
        else:
    elif(r>p)    
