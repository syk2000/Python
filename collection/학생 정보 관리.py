import copy
#메뉴를 출력
#1. 학생 등록
#2. 학생 점수 등록
#3. 학생 정보 출력
#4. 학생 순위순 표기
#5. 종료

def p_menu():
    print("""
1. 학생 등록
2. 학생 점수 등록
3. 학생 정보 출력
4. 학생 순위순 표기
5. 종료
""")#메뉴 출력

def sel_1(name, age):
    stu_l.append([name, age,0])
def sel_3(num):
    print("%s번 학생 | 이름 : %s | 나이 : %d |점수 : %d\n"
        %(n,stu_l[n][0],stu_l[n][1],stu_l[n][2]))
def sel_2(stu_n, point):
    stu_l[stu_n][2] = point
def sel_4():
    tmp = copy.deepcopy(stu_l)
    l = len(tmp)
    for i in range(l-1):
        for j in range(i+1,l):  #선택한것 뒤 부터, 끝까지 비교
            if tmp[i][2] < tmp[j][2]:   #선택한것이 더 크다면
                tmp[i],tmp[j] = tmp[j],tmp[i]
                #tmp = ls[i]       #더 작은값을 앞으로 이동
                #ls[i] = ls[j]
                #ls[j] = tmp
    print(tmp)
#학생 등록시, 학생의 정보는 이름, 나이
stu_l=[]
while(True):
    p_menu()
    sel = int(input())
    if(sel == 1):
        name=input("학생 이름 : ")
        age=int(input("학생 나이 : "))
        sel_1(name, age)
    elif(sel == 3):
        n = int(input("확인하고자 하는 학생 번호 입력 : "))
        sel_3(n)
    elif(sel == 2):
        n = int(input("등록하고자 하는 학생 번호 입력 : "))
        p = int(input("해당 학생의 점수 : "))
        sel_2(n, p)
        #학생별 점수 입력
    elif(sel == 5):
        break
        #마침
    elif(sel ==4):
        sel_4()

    
