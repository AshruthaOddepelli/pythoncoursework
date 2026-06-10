'''
s='looping statement'
for i in s:
    if i in 'aeiouAEIOU':
        print(i)
        


l=[24,26,32,73,76,86,85,7,92,54,66]
for i in l:
    if i%2==0:
        print(i)
        


d={'laptop':0,'charger':2,'keyword':10,'phone':15,'tab':0}
for i in d:
    if d[i]:
        print(i)


t=(9,2,13,4,5,6)
#0 2 26 12 20 30
for i in range(len(t)):
    print(i*t[i])
    
'''  
names = {'subbu','ashrutha','dinesh','panda'}
for i in names:
    print(i.upper(i))