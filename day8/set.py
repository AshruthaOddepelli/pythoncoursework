Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={1,2,3,4}
s=set()
s={1,1,1,1,1}
s
{1}
s={345,456,456,67,2,3,4,5,}
s
{2, 3, 4, 5, 67, 456, 345}
s.set()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.set()
AttributeError: 'set' object has no attribute 'set'
s=set()
s
set()
s.add(1)
s
{1}
s.add(3)
s
{1, 3}
s.add(45.56)
s
{1, 3, 45.56}
s.add('dfgh')
s
{1, 3, 'dfgh', 45.56}
s.add([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.add([1,2,3,4])
TypeError: unhashable type: 'list'
s.add(set())
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.add(set())
TypeError: unhashable type: 'set'
s.add({1:2}{3:4})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s.add({1:2},{3:4})
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s.add({1:2},{3:4})
TypeError: set.add() takes exactly one argument (2 given)
s
{1, 3, 'dfgh', 45.56}
1 in s
True
'dfgh' not in s
False
234 not in s
True
a={1,2,3,4,5,6,7,8,10}
b={6,7,8,9}
a | b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a.intersection(b)
{8, 6, 7}
a & b
{8, 6, 7}
a ^ b
{1, 2, 3, 4, 5, 9, 10}
a - b
{1, 2, 3, 4, 5, 10}
b-a
{9}
a
{1, 2, 3, 4, 5, 6, 7, 8, 10}
#{1}{2}{3}{5}{6}{7}{1,3}{8,10}
a<={1}
False
a>={1}
True
a>={3}
True
a
{1, 2, 3, 4, 5, 6, 7, 8, 10}
b
{8, 9, 6, 7}
a.isdisjoint(b)
False
a.isdisjoint({90,80})
True
a
{1, 2, 3, 4, 5, 6, 7, 8, 10}
a.add(17)
a
{1, 2, 3, 4, 5, 6, 7, 8, 10, 17}
a.add(18)
a
{1, 2, 3, 4, 5, 6, 7, 8, 10, 17, 18}
a.update({12,30,15})
a
{1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 15, 17, 18, 30}
a.pop()
1
a.pop()
2
a
{3, 4, 5, 6, 7, 8, 10, 12, 15, 17, 18, 30}
a.remove(6)
a
{3, 4, 5, 7, 8, 10, 12, 15, 17, 18, 30}
a.remove(8)
a
{3, 4, 5, 7, 10, 12, 15, 17, 18, 30}
a.discard(5)
a
{3, 4, 7, 10, 12, 15, 17, 18, 30}
a.dicard(5)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.dicard(5)
AttributeError: 'set' object has no attribute 'dicard'. Did you mean: 'discard'?
a.discard(5)
a
{3, 4, 7, 10, 12, 15, 17, 18, 30}
a.discard(10)
a
{3, 4, 7, 12, 15, 17, 18, 30}
a.clear()
a
set()


>>> a={1,2,23,57,235}
>>> a
{1, 2, 23, 57, 235}
>>> b={1,2,4,34}
>>> b
{1, 2, 4, 34}
>>> a.intersection(b)
{1, 2}
>>> a
{1, 2, 23, 57, 235}
>>> b
{1, 2, 4, 34}
>>> a.intersection_update(b)
>>> a
{1, 2}
>>> b
{1, 2, 4, 34}
>>> c=b
>>> c.add(12)
>>> c
{1, 2, 34, 4, 12}
>>> a.copy(c)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a.copy(c)
TypeError: set.copy() takes no arguments (1 given)
>>> c
{1, 2, 34, 4, 12}
>>> b
{1, 2, 34, 4, 12}
>>> d=c.copy()
>>> d.add(10)
>>> d
{1, 2, 34, 4, 10, 12}
>>> c
{1, 2, 34, 4, 12}
>>> len(c)
5
>>> min(c)
1
>>> max(c)
34
>>> sorted(c)
[1, 2, 4, 12, 34]
>>> sum(c)
53
