Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> path = "C:\Users\KGITBank\\Desktop\\"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> path ="C:\Users\KGITBank\\Desktop\\"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> file=open(path+"test.txt")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    file=open(path+"test.txt")
NameError: name 'path' is not defined
>>> file=open(path+"test.txt",r)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    file=open(path+"test.txt",r)
NameError: name 'path' is not defined
>>> tmp=file.read()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tmp=file.read()
NameError: name 'file' is not defined
>>> tmp
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tmp
NameError: name 'tmp' is not defined
>>> def xor(n,key):
	l=[]
	for i in n:
		l.append(chr(ord(i)^key))
	return l

>>> xor(tmp,10)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    xor(tmp,10)
NameError: name 'tmp' is not defined
>>> import pickle
>>> fil2=open(path+"dump","wb")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    fil2=open(path+"dump","wb")
NameError: name 'path' is not defined
>>> a = xor(tmp,10)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a = xor(tmp,10)
NameError: name 'tmp' is not defined
>>> a
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 
