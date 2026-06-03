Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=' hello world "
SyntaxError: incomplete input
s=' hello world '
s
' hello world '
s.strip()
'hello world'
s.lstrip()
'hello world '
s.rstrip()
' hello world'
s='sting.py'
s.startswith('str)
             
SyntaxError: incomplete input
s.startswith
             
<built-in method startswith of str object at 0x000002C88677C5B0>
s.startswith(str)
             
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.startswith(str)
TypeError: startswith first arg must be str or a tuple of str, not type
s='sting.py'
             
s
             
'sting.py'
s.startswith(s)
             
True
s.startswith(dfgh)
             
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s.startswith(dfgh)
NameError: name 'dfgh' is not defined
s.endswith('py')
             
True
s.endswith('sdfg')
             
False
'dfgh'.isalpha()
             
True
'WERTY'.isaplha()
             
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    'WERTY'.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
'WERTY'.isalpha()
             
True
'12345'.isalnum()
             
True
'123@345'.isalnum()
             
False
'qwertyui'.islower()
...              
True
>>> 'asdfgh@#$%'.islower()
...              
True
>>> 'SDFGH'.isupper()
...              
True
>>> 'SDFGHJK2345'.isupper()
...              
True
>>> ' '.space
...              
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    ' '.space
AttributeError: 'str' object has no attribute 'space'. Did you mean: 'isspace'?
>>> 
>>> 
>>> ' '.space()
...              
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    ' '.space()
AttributeError: 'str' object has no attribute 'space'. Did you mean: 'isspace'?
>>> ' '.isspace()
...              
True
>>> ''.isspace()
...              
False
>>> 'dfgh    '.isspace()
...              
False
>>> 'Py Ty Lg'.istitle()
...              
True
>>> 'we ert'.islower()
...              
True
>>> 'py_python'.isidentifier
...              
<built-in method isidentifier of str object at 0x000002C886786070>
>>> 'py_python'.isidentifier()
...              
True
