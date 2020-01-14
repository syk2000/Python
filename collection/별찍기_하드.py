n =20
for i in range(n): #5번 반복, 5줄 이므로
    if(i<(n/2-0.5)): #* 갯수는 5/2  번째 줄 까지 증가
        for j in range(int(n/2-0.1) - i):
            #*이 증가하는 동안, ' ' 는 감소(1개씩)
            print(" ", end = '')
        for k in range(i*2+1):
            #*은 2개씩 증가
            print("*", end = '')
    else:
        for j in range(round(i-n/2+0.1)):
            #*이 감소하는 동안, i는 1개씩 증가
            print(" ", end ='')
        for k in range(int((n-i)*2-0.1)):
            print("*", end ='')
    print("")
