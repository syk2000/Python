>>> sys.path
['', 'C:\\Users\\KGITBank\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\idlelib', 'C:\\Users\\KGITBank\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip', 'C:\\Users\\KGITBank\\AppData\\Local\\Programs\\Python\\Python37\\DLLs', 'C:\\Users\\KGITBank\\AppData\\Local\\Programs\\Python\\Python37\\lib', 'C:\\Users\\KGITBank\\AppData\\Local\\Programs\\Python\\Python37', 'C:\\Users\\KGITBank\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages']
>>> import numpy
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    import numpy
ModuleNotFoundError: No module named 'numpy'

# cmd 창에서 pip install numpy이라고 입력을 하면 다운을 받는다.

>>> import numpy
>>> numpy.random.rand(10,2)
array([[0.08245123, 0.04582177],
       [0.72780839, 0.98047718],
       [0.01941954, 0.61265025],
       [0.90260307, 0.26206065],
       [0.85598944, 0.7854543 ],
       [0.00962341, 0.94595921],
       [0.79702613, 0.66516022],
       [0.99058074, 0.11301256],
       [0.96447427, 0.01548463],
       [0.84523446, 0.75500648]])

>>> file = open("test.txt","w")
>>> file.write("hello world")
11
>>> file.close
<built-in method close of _io.TextIOWrapper object at 0x00000200A3DC11F8>
>>> file.close()
>>> file = open("test.txt","r")
>>> file.read()
'hello world'

>>> type(file)
<class '_io.TextIOWrapper'>
>>> file.close()

#내용이 저장 되지 않고 껐다 다시키면 reset 된다.
>>> file = open("C:\\Users\\KGITBank\\test.txt","w")
>>> file.write("안녕")
2
>>> file.close()

#내용이 저장되고 reset이 안된다.
>>> file = open("C:\\Users\\KGITBank\\test.txt","r")
>>> file.close()






file = open("C:\\Users\\KGITBank\\test.txt","w")
>>> s=['a','bb','vcc']
>>> s
['a', 'bb', 'vcc']
>>> file.writelines(s)
>>> file.close()


>>> file = open("C:\\Users\\KGITBank\\test.txt","r")
>>> file.read(1)
'a'
>>> file.read(1)
'b'
>>> file.readlines() #메모장에 있는 내용을 읽게 해주는 것 
['bvcc']

#한줄에 있는 내용이 차례로 출력이 된다.
>>> for i in rile:
	print(i)

#현재 어디까지 읽었는지 알려준다.
>>> file.tell()
6

>>> file.seek(2)
2
>>> file.readline()
'bvcc'
>>> file.tell()
6
>>> file = open("C:\\Users\\KGITBank\\test.txt","a")
>>> file.tell()
6

try:
    file=open("test.txt","w+")
    file.write('''동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이 보전하세~!!!''')

except Exception as e:
    print(e)

finally:
    file.close()

try:
    file=open("test.txt","r")
    #내용을 while문 으로 한줄씩 출력해 주세요
    #그냥 print만 하면, 엔터가 두번씩 써지는 것 주의
    #따라서 end='' 사욜 필수

    
    for s in file():
        print(s.end='')
'''
    s=" "
    for i in file.readlines():
        print(s.end='')
    '''
    '''
    s=" "
    while(s!=''):
        s=file.readline()
        print(s.end='')
        '''
'''
    while(true):
        s = file.readline()
        if(s==''):
            break
        else:
            print(s.end='')
'''
#=============================================================================

>>> fil2=open("C:\\Users\\KGITBank\\test01.txt","wb")
>>> fil2.write(tmp)
6
>>> fil2.close()
#===============================================================================
#이미지 활용
import PIL
from PIL import Image
im=Image.open("경로")
im.show()
Image(tmp)
im.close()
#-------------------------------------------------------------------------------
>>> ord("h")
104
>>> chr(104)
'h'
>>> for i in s:
	tmp = ord(i)
	s_s.append(chr(ord(i)^key))

#=============================================================================
def xor (data,key):
    tmp = []
    for i in data:
        tmp.append(chr(ord(i)^key))
    return ''.join(tmp)

a="hello"
b= xor(a,25)
b

b=xor(b,25)
b="hello"


