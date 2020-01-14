import pickle

def reg_goods(name, price):
    while(goods.get(name) != None):
        print("이미 있는 상품명 입니다.")
        name = input("다시 입력 (취소는 1) : ")
        if( name =='1'):
            return
    goods[name] =price
    

def edit_goods(name, price):
    while(goods.get(name) == None):
        print("없는 상품명 입니다.")
        tmp = input("다시 입력, 추가는 0, 취소는 1 :")
        if(tmp == '1'):
            return
        elif(tmp == '0'):
            break
        else:
            name = tmp

    goods[name] =price


            
def print_goods():
    print("============MENU============")
    for name, price in goods.items():
        print("+%-13s%12s\\+"%(name, price))
    print("============================")


def bill():
    #구매 상품 등록
    #ins = ''
    li = []
    while(True):
        ins = input("구매한 상품을 등록해 주세요")
        if(ins == ''):
            break
        elif(goods.get(ins) == None):
            print("해당 상품이 없습니다.")
            continue
        li.append(ins)
    #구매 상품 가격 합산
    #print(li)
    res = 0

    print("============BILL============")
    for i in li:
        res += goods[i]
        print("+%-13s%12s\\+"%(i, goods[i]))
    print("+%-13s%12s\\+"%("총 계",  res))
    print("============================")
    
def menu():
    print("1. 상품 추가\n2. 상품 가격 수정\n"+
          "3. 메뉴판 출력\n4. 계산서 발행\n5. 종료")
    
    sel = int(input())
    if(sel == 1):
        name = input("상품 이름을 입력해 주세요")
        price = int(input("상품 가격을 입력해 주세요"))
        reg_goods(name, price)
        return True
    elif(sel == 2):
        name = input("상품 이름을 입력해 주세요")
        price = int(input("상품 가격을 입력해 주세요"))
        edit_goods(name, price)
        return True
    elif(sel == 3):
        print_goods()
        return True
    elif(sel == 4):
        bill()
        return True
    elif(sel == 5):
        try:
            file = None
            file = open("menu.csv", "w")
            for i in goods.keys():
                file.write(i+", ")
                file.write(str(goods[i])+"\n")
                #file.write("%s, %d\n"%(i,goods[i]))
        except Exception:
            print("메뉴 저장 실패")
        finally:
            if(file):
                file.close()
            
        return False
    else:
        menu()

try:
    file = None
    file = open("menu.csv", "r")
    goods = {}
    tmp = file.readlines()
    for s in tmp:
        name, price = s.strip("\n").split(',')
        goods[name] = price
except Exception as e:
    print(e)
    goods = {"제육":4500, "짜장면":5000}
finally:
    if(file):
        file.close()
    
while(menu()):
    pass
