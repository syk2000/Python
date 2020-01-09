def xor (data,key):
    tmp = []
    for i in data:
        tmp.append(chr(ord(i)^key))
    return ''.join(tmp)


