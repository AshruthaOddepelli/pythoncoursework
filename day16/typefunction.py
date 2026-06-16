#position
'''
def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("password:",pwd)

display('ashu','Ashrutha@gmail.com','Ashu1@_')
display('Ashu1@_','Ashrutha@gmail.com','ashu')
display('Ashrutha@gmail.com','ashu','Ashru1@_')

o/p:
    
Name: ashu
Email: Ashrutha@gmail.com
password: Ashu1@_
Name: Ashu1@_
Email: Ashrutha@gmail.com
password: ashu
Name: Ashrutha@gmail.com
Email: ashu
password: Ashru1@_

'''
#keyword
'''
def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("password:",pwd)

display(name='ashu',email='Ashrutha@gmail.com',pwd='Ashu1@_')
display(pwd='Ashu1@_',email='Ashrutha@gmail.com',name='ashu')
display(email='Ashrutha@gmail.com',name='ashu',pwd='Ashru1@_')

0/p:
    
Name: ashu
Email: Ashrutha@gmail.com
password: Ashu1@_
Name: ashu
Email: Ashrutha@gmail.com
password: Ashu1@_
Name: ashu
Email: Ashrutha@gmail.com
password: Ashru1@_
'''
#default
'''

def display(name,email,pwd=''):
    print("Name:",name)
    print("Email:",email)
    print("password:",pwd)

display('ashu','Ashrutha@gmail.com','Ashu1@_')
display('Ashrutha@gmail.com','ashu')

0/p:
Name: ashu
Email: Ashrutha@gmail.com
password: Ashu1@_
Name: Ashrutha@gmail.com
Email: ashu
password: 

'''
#variable
'''
def display(*names):
    print("Names:",names)
    

display('ashu','akhila','hansika','tejashwini')
display('komalatha','bhargavi')
display('akhila','supriya','dinesh')
o/p:
Names: ('ashu', 'akhila', 'hansika', 'tejashwini')
Names: ('komalatha', 'bhargavi')
Names: ('akhila', 'supriya', 'dinesh')
'''

'''
def display(**names):
    print("Names:",names)
    

display(k1='ashu',k2='akhila',k3='hansika',k4='tejashwini')
display(k1='komalatha',k2='bhargavi')

output:
    
Names: {'k1': 'ashu', 'k2': 'akhila', 'k3': 'hansika', 'k4': 'tejashwini'}
Names: {'k1': 'komalatha', 'k2': 'bhargavi'}

'''











