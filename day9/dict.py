Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={}
>>> d=dict()
>>> type(d)
<class 'dict'>
>>> d[1]='int'
>>> d
{1: 'int'}
>>> d[1.23]='float'
>>> d
{1: 'int', 1.23: 'float'}
>>> d[1+30j]='complex'
>>> d
{1: 'int', 1.23: 'float', (1+30j): 'complex'}
>>> d[[1,2,3]]='list'
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d[[1,2,3]]='list'
TypeError: unhashable type: 'list'
>>> d[{1,2,3}]='set'
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d[{1,2,3}]='set'
TypeError: unhashable type: 'set'
>>> d[(1,2,3)]='tuple'
>>> d
{1: 'int', 1.23: 'float', (1+30j): 'complex', (1, 2, 3): 'tuple'}
>>> d[False]='bool'
>>> d
{1: 'int', 1.23: 'float', (1+30j): 'complex', (1, 2, 3): 'tuple', False: 'bool'}
>>> d=[1,2]
>>> d=[1.23]
>>> d=[1+2j]
>>> d=[(1,2,3)]
>>> d=[{1,2,5}]
>>> d=[[1,5,6]]
>>> d=['ertyu']
>>> d=[{1:2}]
>>> d=False
>>> d
False
>>> d[1]=[1,2]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d[1]=[1,2]
TypeError: 'bool' object does not support item assignment
>>> d[1]=1,2
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    d[1]=1,2
TypeError: 'bool' object does not support item assignment
>>> d={}
>>> d[20]=23.3
>>> d[2]='sdfghj'
>>> d[3]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    d[3]
KeyError: 3
>>> d[4]=3+4j
>>> d[5]=[1,2,3]
>>> d[6]=(1,2,3)
>>> d[7]={1,3}
>>> d[8]={1:2,1:3}
>>> d[9]=False
>>> d
{20: 23.3, 2: 'sdfghj', 4: (3+4j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 3}, 8: {1: 3}, 9: False}
>>> d={}
>>> d[1]=2
>>> d[2]=2
>>> d[3]=2
>>> d[4]=2
>>> d
{1: 2, 2: 2, 3: 2, 4: 2}
>>> d
{1: 2, 2: 2, 3: 2, 4: 2}
>>> d+d
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d+d
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> d*4
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    d*4
TypeError: unsupported operand type(s) for *: 'dict' and 'int'
>>> d={}
>>> d={1:2,2:4,3:6,4:8,5:10}
>>> d[4]
8
>>> d[8]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    d[8]
KeyError: 8
>>> d={}
>>> d={'komalatha':50,'bhagravi':90,'manoj':99,'ashrutha':56,'dinesh':78}
>>> d['manoj']
99
>>> d['ashrutha']
56
>>> d['supriya']
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    d['supriya']
KeyError: 'supriya'
>>> d.get('supriya'0
      
SyntaxError: invalid syntax
>>> d.get('supriya')
>>> d.get('bhagrvi')
>>> d.get('akhil','user not found')
'user not found'
>>> d.get('manoj','user not found')
99
>>> d
{'komalatha': 50, 'bhagravi': 90, 'manoj': 99, 'ashrutha': 56, 'dinesh': 78}
>>> 'manoj' in d
True
>>> bhagravi not in d
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    bhagravi not in d
NameError: name 'bhagravi' is not defined
>>> bhagravi not in d
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    bhagravi not in d
NameError: name 'bhagravi' is not defined
>>> bhagravi not in d
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    bhagravi not in d
NameError: name 'bhagravi' is not defined
>>> 'bhagravi' not in d
False
>>> d
{'komalatha': 50, 'bhagravi': 90, 'manoj': 99, 'ashrutha': 56, 'dinesh': 78}
>>> d.keys()
dict_keys(['komalatha', 'bhagravi', 'manoj', 'ashrutha', 'dinesh'])
>>> d.value()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    d.value()
AttributeError: 'dict' object has no attribute 'value'
>>> d.values()
dict_values([50, 90, 99, 56, 78])
>>> d.items()
dict_items([('komalatha', 50), ('bhagravi', 90), ('manoj', 99), ('ashrutha', 56), ('dinesh', 78)])
>>> sorted(d)
['ashrutha', 'bhagravi', 'dinesh', 'komalatha', 'manoj']
>>> min(d)
'ashrutha'
>>> max(d)
'manoj'
>>> len(d)
5
>>> d
{'komalatha': 50, 'bhagravi': 90, 'manoj': 99, 'ashrutha': 56, 'dinesh': 78}
>>> d['dinesh']
78
>>> d['dinesh']=100
>>> d
{'komalatha': 50, 'bhagravi': 90, 'manoj': 99, 'ashrutha': 56, 'dinesh': 100}
>>> d['rishi']=67
>>> d
{'komalatha': 50, 'bhagravi': 90, 'manoj': 99, 'ashrutha': 56, 'dinesh': 100, 'rishi': 67}
>>> d.update({'parneeth':90,'ajay':80})
>>> d
{'komalatha': 50, 'bhagravi': 90, 'manoj': 99, 'ashrutha': 56, 'dinesh': 100, 'rishi': 67, 'parneeth': 90, 'ajay': 80}
>>> d.popitem()
('ajay', 80)
>>> d
{'komalatha': 50, 'bhagravi': 90, 'manoj': 99, 'ashrutha': 56, 'dinesh': 100, 'rishi': 67, 'parneeth': 90}
>>> d.pop('manoj')
99
>>> d
{'komalatha': 50, 'bhagravi': 90, 'ashrutha': 56, 'dinesh': 100, 'rishi': 67, 'parneeth': 90}
>>> del d('parneeth')
SyntaxError: cannot delete function call
>>> del d['parneeth']
>>> d
{'komalatha': 50, 'bhagravi': 90, 'ashrutha': 56, 'dinesh': 100, 'rishi': 67}
>>> del d['rishi]
      
SyntaxError: EOL while scanning string literal
>>> 
KeyboardInterrupt
>>> del d['ashrutha']
>>> d
{'komalatha': 50, 'bhagravi': 90, 'dinesh': 100, 'rishi': 67}
>>> d.clear
<built-in method clear of dict object at 0x000001BDD883F5C0>
>>> d.clear()
>>> d
{}
>>> 'manoj'
'manoj'
>>> d={'komalatha': 50, 'bhagravi': 90, 'manoj': 99, 'ashrutha': 56, 'dinesh': 78}
>>> d
{'komalatha': 50, 'bhagravi': 90, 'manoj': 99, 'ashrutha': 56, 'dinesh': 78}
>>> d.setdefault('manoj',0)
99
>>> d
{'komalatha': 50, 'bhagravi': 90, 'manoj': 99, 'ashrutha': 56, 'dinesh': 78}
>>> d.setdefault('chutkii',87)
87
>>> d
{'komalatha': 50, 'bhagravi': 90, 'manoj': 99, 'ashrutha': 56, 'dinesh': 78, 'chutkii': 87}
>>> 
