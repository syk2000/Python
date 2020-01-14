p_id, name = input("주민번호 앞자리와 이름").split()
try:
    if(len(p_id) != 6):
        raise Exception("잘못 입력")
    if(not(p_id.isdigit())):
        raise Exception("숫자 미입력")
    p_year = int(p_id[:2])

    if(not((p_year <= 99 and p_year > 20) or p_year in [0,1])):
        raise Exception("가입 불가능한 나이")
    
    print(p_id, p_year, name)
except Exception as e:#수정 필요
    #try구문에 오류 있을경우 수행
    #print(str(e)+"의 사유로 가입이 불가능 합니다.")
    print("가입이 불가능 합니다.")
    print("사유 : ",e)
    pass
else:
    #try구문에 오류 없을경우 수행
    print("가입을 축하합니다.")
    pass
finally:
    #무조건 수행
    print("가입 프로세스 완료")
    pass
