import random as rd
#가위 바위 보 코드

"""
#메뉴출력
def print_menu():
    pass
"""
code = ["가위","바위","보"]
#가위 바위 보 입력
def ins_rcp():
    ins = int(input("가위 면 0, 바위면 1 보면 2"+
                "를 입력해 주세요"))
    return ins
    

#컴퓨터 가위 바위 보
def com_rcp():
    #랜덤으로 0,1,2 중 하나 리턴
    return rd.randint(0,2)

#승부 결과 출력
def rcp_res(user, com):
    tmp = user-com
    if(tmp == 1 or tmp == -2):
        return 1
    elif(tmp == 0):
        return 0
    else:
        return -1 

#이길 때까지 반복
#컴퓨터는 무조건 바위

#print_menu()
for i in range(5):
    user = ins_rcp()
    print(code[user])
    com = com_rcp()
    res = rcp_res(user, com)
    if(res == -1):
        #유저 패배
        pass
    elif(res == 0):
        #비김
        pass
    elif(res == 1):
        #유저 승리
        pass

#승리/패배/비김 횟수 출력
