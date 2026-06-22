
#genrator
'''

def display():
    l=['1..50','51..100','101..200','201..250']
    yield l[0]
    yield l[1]
    yield l[2]
    yield l[3]
    
scroll=display()

print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
'''
#range (1,10)
'''
def display():
    for i in range(1,11):
        yield i
        
n = display()
for i in range(10):
    print(next(n))

'''
#factors of Yield method
'''
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i
        
n = factors(56)
try:
    while True:
        print(next(n))

except StopIteration:
    print("End of the program")
'''
#another method
'''
def factors(n):
    return [i for i  in range(1,n+1) if n%i==0]

def generatos(res):
    for i in res:
        yield i

res = factors(60)
facts=generatos(res)
for i in range (len(res)):
    print(next(facts))

'''
#primes (2,101) 
'''
def primes():
    res=[]
    for num in range(2,101):
        for i in range(2,num//2+1):
            if num%i==0:
                break
        else:
            res.append(num)

    return res
def generators(res):
    for i in res:
        yield i
res=primes()
g = generators(res)
for i in range(len(res)):
    print(next(g))
                
'''


































