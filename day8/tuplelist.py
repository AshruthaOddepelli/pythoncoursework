Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=()
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=()
t=(1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t=(1,1.1,'tyu',[])
t
(1, 1.1, 'tyu', [])
t=(10,20,30,40,50)
t
(10, 20, 30, 40, 50)
h=(70,80,90)
h
(70, 80, 90)
t+h
(10, 20, 30, 40, 50, 70, 80, 90)
t
(10, 20, 30, 40, 50)
t=t+h
t
(10, 20, 30, 40, 50, 70, 80, 90)
t[0]
10
t[-1]
90
t[4]
50
t[-3]
70
t[:2]
(10, 20)
t[::-1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
t[::-1]
(90, 80, 70, 50, 40, 30, 20, 10)
t[1:3:2]
(20,)
t[2:5]
(30, 40, 50)
10 not in t
False
50 in t
True
80 not in t
False
t[2:]
(30, 40, 50, 70, 80, 90)
t[-1:-4:-1]
(90, 80, 70)
t
(10, 20, 30, 40, 50, 70, 80, 90)
len
<built-in function len>
len(t)
8
sorted(t)
[10, 20, 30, 40, 50, 70, 80, 90]
max(t)
90
min(t)
10
sum(t)
390
t.conut(10)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    t.conut(10)
AttributeError: 'tuple' object has no attribute 'conut'. Did you mean: 'count'?
t.count(10)
1
t.index(10)
0
a=(1,2,3)
a
(1, 2, 3)
a,b,c=1,2,3
a
1
b
2
>>> c
3
>>> x,y,z=a
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x,y,z=a
TypeError: cannot unpack non-iterable int object
>>> a=(1,2,3)
>>> a
(1, 2, 3)
>>> x,y,z=a
>>> x
1
>>> y
2
>>> z
3
>>> t=(1,2,3,,[4,5,6],7,8)
SyntaxError: invalid syntax
>>> t=(1,2,3,[4,5,6],7,8)
>>> t
(1, 2, 3, [4, 5, 6], 7, 8)
>>> t[2]
3
>>> t[4]
7
>>> t[3]
[4, 5, 6]
>>> t[2]
3
>>> t[2].append(10)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    t[2].append(10)
AttributeError: 'int' object has no attribute 'append'
>>> t[4].append(10)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    t[4].append(10)
AttributeError: 'int' object has no attribute 'append'
>>> t[3]
[4, 5, 6]
>>> t[3].append(10)
>>> t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
