
#py pt ph po pn yt yh yo yn th to tn ho hn 
'''
s='python'
for i in range(len(s)):
    for j in range(len(s)):
        print(s[i],s[j],sep='',end=' ')

'''
'''
#sum=45
l=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
for i in l:
    for j in i:
        sum+=j
print(f'sum={sum}')

'''
d={
    '1234':{'pin':'4557','balance':2300},
    '5676':{'pin':'6782','balance':9300},
    '7860':{'pin':'2346','balance':5300},
    '3409':{'pin':'0977','balance':8300}

    }
for i in d:
    print('Account number:',i)
    print('pin number:',d[i]['pin'])
    
