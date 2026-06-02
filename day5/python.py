Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name=input()
ashrutha
>>> name
'ashrutha'
>>> name=("enter your name")
>>> enter your name
SyntaxError: invalid syntax
>>> name=("enter your name :")
>>> enter your name: ashrutha
SyntaxError: invalid syntax
>>> name= input("enter your name :")
enter your name :ashu
>>> name
'ashu'
>>> KeyboardInterrupt
>>> age= input("enter your age :")
enter your age :21
>>> age
'21'
>>> age=int(input("enter your age: '))
...               
SyntaxError: incomplete input
>>> age=int(input("enter your age: "))
...               
enter your age: 21
>>> age
...               
21
>>> gpa=float(input("enter your name:"))
...               
enter your name: 7.3
>>> gpa
...               
7.3
>>> 'ashrutha vaishnavi bhargavi komali'
...               
'ashrutha vaishnavi bhargavi komali'
>>> 'ashrutha vaishnavi bhargavi komali'.split(' ')
...               
['ashrutha', 'vaishnavi', 'bhargavi', 'komali']
>>> 'java-python-c-c++-javascript'.split
...               
<built-in method split of str object at 0x00000231884C6240>
>>> 'java-python-c-c++-javascript'.split()
...               
['java-python-c-c++-javascript']
products= input("enter the products:"))
        
SyntaxError: unmatched ')'
products= input("enter the products:").split()
        
enter the products:laptop keyboard charger mouse
products
        
['laptop', 'keyboard', 'charger', 'mouse']
topics = tuple(input("enter the topics: ").split()
 topics = tuple(input("enter the topics: ").split()
                
SyntaxError: invalid syntax. Perhaps you forgot a comma?
 topics = tuple(input("enter the topics: ").split())
                
SyntaxError: unexpected indent
topics = tuple(input("enter the topics: ").split())
                
enter the topics: token statement variable comments
topics
                
('token', 'statement', 'variable', 'comments')
op=set(input("enter the oper: ").split())
                
enter the oper: is not not in is and or not
op
                
{'and', 'or', 'in', 'not', 'is'}
list(map(int,input("enter the marks:").split()))
                
enter the marks:1 2 3 55 345
[1, 2, 3, 55, 345]
prices=tuple(map(int,input("enter the prices:").split()))
                
enter the prices:234 45567 678 78
prices
                
(234, 45567, 678, 78)
rating=set(map(int,input("enter the rating:").split()))
                
enter the rating:4 3 4 5 3 3 1 2
rating
                
{1, 2, 3, 4, 5}
per =list(map(float,input("Enter the per's :").split()))
                
Enter the per's :56.3 23.3 78.9 
per
                
[56.3, 23.3, 78.9]
price =tuple(map(float,input("Enter the price :").split()))
                
Enter the price :345 456 5678 567
price
                
(345.0, 456.0, 5678.0, 567.0)
price =set(map(float,input("Enter the price :").split()))
                
Enter the price :345 456 567 678
price
                
{456.0, 345.0, 678.0, 567.0}
a,b = 10 , 20
                
a
                
10
b
                
20
a,b = (10 , 20)
                
a
                
10
b
                
20
a,b = [10 , 20]
                
a
                
10
b
                
20
username,password = input("Enter the username & password: ").split()
                
Enter the username & password: ashrutha a@123
username
                
'ashrutha'
password
                
'a@123'
a,b,c,d=list(map(int,input("enter 4 sides: ").split()))
                
enter 4 sides: 12 3 4 5
a
                
12
b
                
3
c
                
4
d
                
5
price,discount=list(map(float,input("enter 4 sides: ").split()))
                
enter 4 sides: 
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    price,discount=list(map(float,input("enter 4 sides: ").split()))
ValueError: not enough values to unpack (expected 2, got 0)
price,discount=list(map(float,input( ).split()))
                
234556 45.0
price
                
234556.0
discount
                
45.0
a=eval(input())
                
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a=eval(input())
KeyboardInterrupt
a=eval(input())
                
3456
a
                
3456
a=eval(input())
                
23456.5678
a
                
23456.5678
a=eval(input())
                
"python"
a
                
'python'
a=eval(input())
                
[1,2,3,4,5]
a
                
[1, 2, 3, 4, 5]
a=eval(input())
                
{1,2,3,4,6,6}
a
                
{1, 2, 3, 4, 6}
a=eval(input())
                
{2:3,3:6,7:8
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1
    {2:3,3:6,7:8
    ^
SyntaxError: '{' was never closed
}
{2:3,3:6,7:8}
 
{2: 3, 3: 6, 7: 8}
a=eval(input())
 
true
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
a=eval(input())
 
True
a
 
True
class(a)
SyntaxError: invalid syntax
type(a)
<class 'bool'>
