import copy
stu_i=[]

while(True):
    print("1. 학생등록 \n2.학생 점수 등록\n3.학생 정보출력\n4.학생순위순 표기\n5.종료")
    sel = int(input())
    if(sel==1):
        name = input("학생의 이름을 등록하세요~!!!")
        age = input("학생의 나이를 입력하세요~!!!")
        stu_i.append([name,age,0])
    elif(sel==2):
        n= int(input("등록하고자 하는 학생 번호 입력: "))
        sc = int(input("점수를 등록하세요~!!!"))
        stu_i[n][2] = sc
    elif(sel==3):
        n= int(input("확인하고자 하는 학생 번호 입력:"))
        print("%s번 학생 | 이름 : %s |나이: %s|점수: %s"%(n.stu_i[n][0],n.stu_i[n][1],n.stu_i[n][2]))
    elif(sel==4):
        print("학생 순위순 표기")
        tmp = copy.deepcopy(stu_i)
        l= len(tmp)
        for i in range(len(stu_i)-1):
            for j in range(i+1,l):
                if(tmp[i][2]<tmp[j][2]):#정순 정렬
                    tmp[i],tmp[j] = tmp[j],tmp[i]
        print(tmp)  
    else:
        break;
        
