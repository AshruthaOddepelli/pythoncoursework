#list comphension (iteration updating insertion) & generator
#directly generate a single line

'''
res1=[]
for i in range(1,11):
    res1.append(i)

res2 = [i for i in range(1,11)]

print(res1)
print(res2)


res3=[]
for i in range(3,31,3):
    res1.append(i)

res4 = [i for i in range(3,31,3)]

print(res3)
print(res4)

res5=[]
for i in range(2,51,2):
    res1.append(i)

res6 = [i for i in range(2,51,2)]

print(res5)
print(res6)

'''

#string
'''
a = 'python programming'
l=[]
for i in a:
    if i in 'aeiouAIEOU':
        l.append(i)

print(l)
l1=[i for i in a if i in 'aeiouAIEOU']
print(l1)
'''
'''
a=[1,2,3,4,5,6,7,8,12,34,56,78,90,42,67,11]
l=[]

for i in a:
    if i%2==0:
        l.append(2)
    else:
        l.append(0)
print(l)

l1=[i if i%2==0 else 0 for i in a]
print(l1)
'''
#
'''
l=[int(input(f"Enter the number - {i+1}: "))for i in range(10)]
print(l)
'''
#nested loop
'''
l=[]
for i in range(3):
    for j in range(1,4):
        l.append(j)
print(l)

l1=[j for i in range(3) for j in range(1,4)]
print(l1)

'''
#matric nested loop
'''
l=[]
for i in range(3):
    temp=[]
    for j in range(1,4):
        temp.append(j)
    l.append(temp)
print(l)

l1=[[j for j in range(1,4)] for i in range(3)]
print(l1)
'''
#set comprehension
'''
s=set()
for i in range(1,11):
    s.add(i)

s1={i for i in range(1,11)}

print(s,s1)

'''
#dict comprehension
'''
d={}
for i in range(1,11):
    d[i]=i*i


print(d)

res={i:i*i for i in range(1,11)}

print(res)

'''
#dict[name]=marks
'''
d={}
for i in range(5):
    names=input()
    marks=int(input())
    d[names]=marks

print(d)

#single line

res={input("enter the name: "):int(input("enter the marks:"))for i in range(5)}
print(res)

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



















































