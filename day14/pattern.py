'''
01010
01010
01010
01010
01010
for row in range(5):
    for col in range(5):
        print(row,end='')
    print()
'''

'''
*
**
***
****
*****
n=int(input("enter the size:"))
for row in range(n):
    for col in range(n):
        print('*',end='')
    print()

'''
'''


n=int(input())
for row in range(n):
    for col in range(n):
        print(col%2,end='')
    print()
'''
'''
*
**
***
****
*****

n=int(input())
for row in range(n):
    for col in range(row+1):
        print('*',end='')
    print()
'''
'''
******
*****
****
***
**
*
n=int(input())
for i in range(n):
    for j in range(n-i):
        print('*',end='')
    print()
'''
'''
#
     ******
    *******
   ********
  *********
 **********
***********
n=int(input())
for i in range(n):
    for sp in range(n-1-i):
        print(' ',end='')
    for j in range(n+i):
        print('*',end='')
    print()
'''

'''
* * * * * 
  * * * * 
    * * * 
      * * 
        *
n=int(input())
for row in range(n):
    for sp in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()

'''
'''
01010
10101
01010
10101
01010

n=int(input())
for i in range(n):
    for j in range(n):
        print((i+j)%2,end='')
    print()

'''
'''
01 
02 03 
04 05 06 
07 08 09 10 
11 12 13 14 15

n=int(input())
c=1
for i in range(n):
    for j in range(i+1):
        print(str(c).zfill(2),end=' ')
        c+=1
    print()

'''




























