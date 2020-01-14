def sq(a):
    try:
        a = int(a)
        print(a*a)
    except Exception as e:
        print(e)
        return None
    else:
        print("문제 없이 수행 되었네요")
    finally:
        print("끗")
    print("try 밖")
    return a*a
