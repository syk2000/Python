goods={}
def reg_goods(name,price):
    while(goods.get(name) !=None):
        print("이미 있는 상품명 입니다.")
        name = input("다시 입력 (취소는 1)")
        if(name == '1'):
            return
    goods[name] = price

def edit_goods(name,price):
    while(goods.get(name) == None):
        print("없는 작품명 입니다.")
        tmp = input("다시 입력. 추가는 0,취소는 1 :")
        if(tmp=='1'):
            return
        elif(tmp=='0'):
            break
        else:
            name = tmp

    goods[name]=  price
'''
def del_goods(name,price):
    while(goods.get(name) != None):
        print("삭제 하시겠습니까?")
        out = input("Yes: 1 ,No: 2")
        if(out==1):

            print("삭제 처리가 되었습니다.")
        else:
            return

    goods[name]=price
'''
def print_goods():
    print("===========================Menu==============================")
    for name, price in goods.items():
        print("+%-13s%13s+"%(name,price))
        print("===============================================================")



def menu():
    print("1. 상품추가 \n2. 상품 가격 수정\n3. 메뉴판 출력\n4. 계산서 발행\n5. 종료")

    sel = int(input())
    if(sel==1):
        name = input("상품 이름을 입력해 주세요")
        price = input("상품 가격을 입력해 주세요")
        reg_goods(name,price)
        return True
    elif(sel ==2):
        name = input("상품 이름을 입력해 주세요")
        price = input("상품 가격을 입력해 주세요")
        reg_goods(name,price)
        return True
    elif(sel==3):
        print_goods()
        return True
    elif(sell==4):
        return True
    elif(sel==5):
        return False
    else:
        
