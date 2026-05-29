Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
a
10
b = 10
type(b)
<class 'int'>
t=999.9
type(t)
<class 'float'>
c=12+8j
type(c)
<class 'complex'>
s='python'
>>> type(s)
<class 'str'>
>>> s="sdfghjkl"
>>> type(s)
<class 'str'>
>>> s='''asdfghjk'''
>>> type(s)
<class 'str'>
>>> l =['post.png','reel.mp4')
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> l =['post.png','reel.mp4']
>>> l
['post.png', 'reel.mp4']
>>> l=[]
>>> l=list()
>>> type(l)
<class 'list'>
>>> t=()
>>> t=(1,2,3,4,5)
>>> t
(1, 2, 3, 4, 5)
>>> type(t)
<class 'tuple'>
>>> s={1,2,3,4,5)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> s={1,2,3,4,5}
>>> type(s)
<class 'set'>
>>> s={34567,456,567}
>>> type(s)
<class 'set'>
>>> d={'name':abc,'age':23,'course':python}
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    d={'name':abc,'age':23,'course':python}
NameError: name 'abc' is not defined. Did you mean: 'abs'?
>>> d={'name':'abc','age':23,'course':'python'}
>>> type(d)
<class 'dict'>
>>> status =True
>>> status =False
>>> type(status)
<class 'bool'>
>>> a = None
>>> type(a)
<class 'NoneType'>
