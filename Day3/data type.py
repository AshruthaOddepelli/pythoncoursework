Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
>>> type(a)
<class 'int'>
>>> t=999.99
>>> type9t)
SyntaxError: unmatched ')'
>>> type(t)
<class 'float'>
>>> c=12=6j
SyntaxError: cannot assign to literal
>>> c=12+6j
>>> type(c)
<class 'complex'>
>>> s='dfghj'
>>> type(s)
<class 'str'>
>>> s="dfgh"
>>> type(s)
<class 'str'>
>>> s='''dfghj'''
>>> type(s)
<class 'str'>
>>> l=[]
>>> l=list()
>>> type(l)
<class 'list'>
>>> t=(1,2,3,4,5)
>>> type(t)
<class 'tuple'>
>>> s={1,2,4,5}
>>> type(s)
<class 'set'>
>>> d={'name':'abg','age':100,'course':'sdf'}
>>> type(d)
<class 'dict'>
>>> status=True
>>> status=False
>>> type(status)
<class 'bool'>
>>> a=none
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a=none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> a=None
>>> type(a)
<class 'NoneType'>
