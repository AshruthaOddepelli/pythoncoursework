Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=20
b=30
a=b
a+b
60
a-b
0
a*b
900
a/b
1.0
a//b
1
a**3
27000
a%b
0
a=20
comparsion
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    comparsion
NameError: name 'comparsion' is not defined
....comparsion
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ....comparsion
AttributeError: 'ellipsis' object has no attribute 'comparsion'
...
Ellipsis
3/4
0.75
a
20
b
30
a>b
False
a<b
True
10<=b
True
a>=b
False
a==b
False
a!=b
True
y=5
y
5
y=y+5
y
10
y=y+10
y
20
y += 10
y
30
y -= 10
y
20
y /= 5
y
4.0
y//=2
y
2.0
y*==10
SyntaxError: invalid syntax
y **= 10
y
1024.0
y = 10
y
10
a
20
b
30
a&b
20
a||b
SyntaxError: invalid syntax
a%10==0
True
a%20==0 and b%20==0 and a>b
False
KeyboardInterrupt
a%20==0 or b%20==0 or a>b
True
a%20==0 and b%20==0 and a<b
False
not a>b
True
#str,list,tuple,set,dict
a='python programming'
'y' in a
True
'g' not in a
False
'r' not in a
False
l=['java','python','mysql','c++','html')
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['

l=['java','python','mysql','c++','html']
l=['java','python','mysql','c++','html']
'java' in l
True
'javascript' not in l
True
'mqsql' not in l
True
t={1,2,3,4,5,6}
5 in t
True
5 not in t
False
set ={'oil':29,'sugar':234,'tea':345}
oil in set
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    oil in set
NameError: name 'oil' is not defined
'oil' in set
True
'tea' not in set
False
d ={'oil':29,'sugar':234,'tea':345}
'oil' in d
True
s=(1,'apple',3)
'apple' in s
True
3 not in s
False
m=[1,2,3,4,5]
l=[1,2,3,4,5]
1==m
False
m==l
True
m=n
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    m=n
NameError: name 'n' is not defined
>>> n=m
>>> n
[1, 2, 3, 4, 5]
>>> 1 is m
False
>>> n is m
True
>>> 8&14
8
>>> 8&7
0
>>> 8|7
15
>>> 10^11
1
>>> ~12
-13
>>> 15>>3
1
>>> 14>>7
0
>>> 13<<6
832
>>> 16<<1
32
>>> print("a=",a,'b=',b,'c=',c,sep='',end='@@@@')
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    print("a=",a,'b=',b,'c=',c,sep='',end='@@@@')
NameError: name 'c' is not defined
>>> a=123
>>> b=12.34
>>> c='python'
>>> set ={'oil':29,'sugar':234,'tea':345}
>>> print("a=",a,'b=',b,'c=',c,sep='',end='@@@@')
a=123b=12.34c=python@@@@
>>> print("a=",a,'b=',b,'c=',c,sep='',end='\n\n')
a=123b=12.34c=python

>>> print(f'a= {a) b={b} c={c}')
SyntaxError: incomplete input
>>> print(f'a= {a) b={b} c={c}')
SyntaxError: incomplete input
