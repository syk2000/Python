Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> li[1,2,3,4]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    li[1,2,3,4]
NameError: name 'li' is not defined
>>> import copy
>>> copy.deepcopy()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    copy.deepcopy()
TypeError: deepcopy() missing 1 required positional argument: 'x'
>>> li=[1,2,3,4]
>>> copy.deepcopy(li)
[1, 2, 3, 4]
>>> from copy import deepcopy
>>> deepcopy(li)
[1, 2, 3, 4]
>>> random.ramdp,()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    random.ramdp,()
NameError: name 'random' is not defined
>>> random.random()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    random.random()
NameError: name 'random' is not defined
>>> random.randrange()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    random.randrange()
NameError: name 'random' is not defined
>>> import rand
