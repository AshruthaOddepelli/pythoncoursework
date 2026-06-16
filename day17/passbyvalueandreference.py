#int float complex str tuple set dict bool
#int float complex str tuple bool -> immutable passing
#list set dict -> mutable


#int
'''
def update(n):
    n+=10
    print("Inside:",n)

n=10
update(n)
print("outside:",n)

#Inside: 20
#outside: 10

'''
#float
'''
def update(n):
    n+=10
    print("Inside:",n)

n=10.4
update(n)
print("outside:",n)
'''
#complex
'''
def update(n):
    n+=10
    print("Inside:",n)

n=3+4j
update(n)
print("outside:",n
'''
#string
'''
def update(n):
    n+='python'
    print("Inside:",n)

n=' lang'
update(n)
print("outside:",n)
'''
#list
'''
def update(n):
    n.append(6)
    print("Inside:",n)

n=[1,2,3,4,5]
update(n)
print("outside:",n)

'''
#tuple
'''
def update(n):
    n+=4
    print("Inside:",n)

n=1,2,3,4,5
update(n)
print("outside:",n)

'''
#set
'''
def update(n):
    n.add(6)
    print("Inside:",n)

n={1,2,3,4,5}
update(n)
print("outside:",n)

'''
#dict
'''
def update(n):
    n+=6
    print("Inside:",n)

n={2:2,3:3,5:2}
update(n)
print("outside:",n)
'''
#bool
'''
def update(n):
    n+=True
    print("Inside:",n)

n=False
update(n)
print("outside:",n)

#Inside: 1
#outside: False

'''







