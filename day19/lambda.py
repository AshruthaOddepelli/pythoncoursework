'''
syntax
 var = lambda arg: expression
'''
# adding(a,b)
'''
add = lambda a,b:a+b
print(add(12,13))
print(add(45,67))
'''
#wish(name)
'''
wish = lambda name: f'welcome to python course {name}'

print(wish('ashrutha'))
print(wish('supriya'))
'''
#gst(price)
'''
gst = lambda price : price + price*0.10

print(gst(1000))
print(gst(299))
print(gst(500))
'''
#greatest number
'''
greatest = lambda a,b:a if a>b else b

print(greatest(100,20))
print(greatest(20,10))
'''
#iseven or odd
'''
iseven = lambda a: f"{a}-even number" if a%2==0 else f"{a}-odd number"

print(iseven(4))
print(iseven(63))
print(iseven(88))
'''
#bill(charge)
'''
bill = lambda charge : charge if charge>99 else charge+50

print(bill(150))
print(bill(50))
print(bill(99))
'''
#login(instock)
'''
login = True
instock = True

status = lambda login,instock: ("you can buy product" if instock else "product is out of stock") if login else "login to buy a product"
print(status(login,instock))

'''
#for loop(list)(map)
'''
l=[1,2,3,4,5]
res=list(map(lambda i:i**3,l))
print(res)
'''
#title format(list) (map)
'''
names=['ashu','pranathi','vyshnavi']
t=list(map(lambda i:i.title(),names))
print(t)
'''
#list(filter)
'''
l=[1,2,3,4,5]
res=list(filter(lambda i:i>3,l))
print(res)
'''
'''
l=[1,2,3,4,5]
res=list(filter(lambda i:i%2==0,l))
print(res)

'''
#reduce->combine in one unit
'''
from functools import reduce
l=[1,2,3,4,5,6,7,8,11]

s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda pro,i:pro*i,l)
m=reduce(lambda max,i: max if max>i else i,l)
mi=reduce(lambda min,i: min if min<i else i,l)
print(s,p,m,mi)

'''
#dict(sorted)
'''

d={'subbu':80,'dinesh':90,'akhil':100,'manoj':90}

print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))

print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))

'''
#dict(tuple)
'''
d={'salt':80,'sugar':90,'milk':100,'chilli':90}

res=list(map(lambda i: (i[0],i[1]+i[1]*0.18),d.items()))
res1=list(map(lambda i: (i[0],i[1]-i[1]*0.5),d.items()))

print(res)
print(res1)
'''
#fliter (greater than less than)'''
d={'salt':20,'sugar':90,'milk':100,'chilli':90}

res=dict(filter(lambda i:i[1]>50,d.items()))
res1=dict(filter(lambda i:i[1]<50,d.items()))

print(res)
print(res1)
'''















