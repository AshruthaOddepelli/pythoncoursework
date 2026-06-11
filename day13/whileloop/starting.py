'''
i=11
while i<11:
    print(i)
    i+=1
    
i=2
while i<21:
    print(i)
    i+=2
    
i=10
while i>10:
    print(i)
    i-=1
  
i=5
while i<51:
    print(i)
    i+=5
    
l=[1,2,3,4,5,6,7,8,9]
i=0
while i<len(l):
    print(l[i])
    i+=1

l='python programming'
i=0
while i<len(l):
    print(l[i])
    i+=1

l=(1,2,3,45,5,6,7)
i=0
while i<len(l):
    print(l[i])
    i+=1
    


l=[0,0,0,0,1,2,34,5,0,0,0,0,0]
while 0 in l:
    l.remove(0)
print(l)

'''
moves=int(input())
while moves>1:
    status=input("[w]in or [c]continue :").upper()
    if status == 'W':
        print("You Win the game")
        break
    moves-=1
    print(f'{moves} moves are left')
else:
    print("Game over")