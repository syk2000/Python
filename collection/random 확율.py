from random import randint
import pprint
n = 100000
dic={}
for i in range(n):
    tmp = randint(1,10)
    dic[tmp] = dic.setdefault(tmp, 0)+1
    

k = dic.keys()
for i in k:
    dic[i] = "%.1f%%"%(dic[i] / n *100)

pprint.pprint(dic)

