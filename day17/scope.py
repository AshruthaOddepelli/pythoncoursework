'''
 local Scope()
--------------
def display():
    n=10
    print("Inside:",n)
display()
print("outside:",n)

'''
'''
global scope()
--------------
n=10

def display():
    print("Inside:",n)
display()
print("outside:",n)

'''
'''
def display():
    global n
    n=10
    print("Inside:",n)
display()
print("outside:",n)
'''
'''
def display(n):
    #global n
    n+=10
    print("Inside:",n)
n=10
display(n)
print("outside:",n)

Inside: 20
outside: 10
'''
# whenever you passing 
'''
def display():
    global n
    n+=10
    print("Inside:",n)
n=10
display()
print("outside:",n)

Inside: 20
outside: 20
'''
'''
def outer():
    n=10
    def inner(n):
        n+=10
        print("Inner Function:",n)
    inner(n)

    print("Outer Function:",n)

outer()

Inner Function: 20
Outer Function: 10
'''
'''
def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Inner Function:",n)
    inner()

    print("Outer Function:",n)

outer()

Inner Function: 20
Outer Function: 20

'''
'''
# cannot written builtin function as a variable
s='python'
print(len(s))

len=5
print(len(s))

'''






























