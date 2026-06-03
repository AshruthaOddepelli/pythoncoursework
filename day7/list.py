Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[]
l=list()
type(l)
<class 'list'>
l=[10,20,30,40,50]
m=[4,5,6,7,8]
l+m
[10, 20, 30, 40, 50, 4, 5, 6, 7, 8]
l*2
[10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
l
[10, 20, 30, 40, 50]
l[3]
40
l[0]
10
l[1]
20
l[4]
50
l[::-1]
[50, 40, 30, 20, 10]
l[:3]
[10, 20, 30]
l[:6}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
l[:6]
[10, 20, 30, 40, 50]
l[1:2]
[20]
10 in l
True
10 not in l
False
50 in l
True
80 not in l
True
l
[10, 20, 30, 40, 50]
l[-1:-4:-3]
[50]
l[-1:-4:-1]
[50, 40, 30]
l[-3::-1]
[30, 20, 10]
id(l)
2265430602432
1
1
l
[10, 20, 30, 40, 50]
l.append(120)
l
[10, 20, 30, 40, 50, 120]
l.append(70)
l
[10, 20, 30, 40, 50, 120, 70]
l.insert(1,70)
l
[10, 70, 20, 30, 40, 50, 120, 70]
l.insert(5,400)
l
[10, 70, 20, 30, 40, 400, 50, 120, 70]
l.extend([120,136,345])
l
[10, 70, 20, 30, 40, 400, 50, 120, 70, 120, 136, 345]
l.pop()
345
l
[10, 70, 20, 30, 40, 400, 50, 120, 70, 120, 136]
l.pop(3)
30
l
[10, 70, 20, 40, 400, 50, 120, 70, 120, 136]
l.remove(136)
l
[10, 70, 20, 40, 400, 50, 120, 70, 120]
l.remove(40)
l
[10, 70, 20, 400, 50, 120, 70, 120]
del (20)
SyntaxError: incomplete input
del[20]
SyntaxError: incomplete input
l.del[20]
SyntaxError: invalid syntax
l.del(20)
SyntaxError: invalid syntax
del l[1]
l
[10, 20, 400, 50, 120, 70, 120]
del l[2]
l
[10, 20, 50, 120, 70, 120]
l.clear()
l
[]
l=[200,400,50,33,45,56,78,]
l
[200, 400, 50, 33, 45, 56, 78]
sorted(l)
[33, 45, 50, 56, 78, 200, 400]
l.sort()
l
[33, 45, 50, 56, 78, 200, 400]
min(l)
33
max(l)
400
l.reversr()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    l.reversr()
AttributeError: 'list' object has no attribute 'reversr'. Did you mean: 'reverse'?
l.reverse()
l
[400, 200, 78, 56, 50, 45, 33]
sorted(l,reverse=true)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    sorted(l,reverse=true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> l.sorted(reverse=true)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    l.sorted(reverse=true)
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> l.sorted(reverse=True)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    l.sorted(reverse=True)
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> sorted(l,reverse=True)
[400, 200, 78, 56, 50, 45, 33]
>>> l
[400, 200, 78, 56, 50, 45, 33]
>>> l.index(33)
6
>>> l.index(44)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    l.index(44)
ValueError: 44 is not in list
>>> l.count(78)
1
>>> l.cont(200)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    l.cont(200)
AttributeError: 'list' object has no attribute 'cont'. Did you mean: 'count'?
>>> l.count(200)
1
>>> l
[400, 200, 78, 56, 50, 45, 33]
>>> len
<built-in function len>
>>> len(l)
7
>>> sum(l)
862
>>> # 0 0.0 '' {} [] () False set()
>>> any([1,2,3,4,5,0,0,0])
True
>>> all([2,3,34,5,0,0,0,])
False
