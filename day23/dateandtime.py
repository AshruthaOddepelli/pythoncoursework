'''
from datetime import date

t=date.today()

print(t)
print("Year:",t.year)
print("month:", t.month)
print("Day:", t.day)
print("weekday from 0:", t.weekday())
print("weekday from 1:", t.isoweekday())

'''
#date () for validate the values
'''
from datetime import date

t=date(2010,10,14)
print(t)
'''
#time() for validate the actual value
'''
from datetime import time

t=time(23,59,0)
print(t)
'''
#year,month,day
'''
from datetime import date,time,datetime
n=datetime.now()
print(n)
print("Year:",n.year)
print("month:", n.month)
print("Day:", n.day)
print("Hour:",n.hour)
print("minute:", n.minute)
print("Second:", n.second)
'''
#formatting date and time
'''
from datetime import date,time,datetime
n=datetime.now()
print(n.strftime('%d/%m/%y'))
print(n.strftime('%d/%m/%y %H:%M:%S'))
print(n.strftime('%d/%m/%y %I:%H:%M:%S %p'))
print(n.strftime('%d %b %y %I:%M:%S %p'))
print(n.strftime('%d %B %y %I:%M:%S %p'))
print(n.strftime('%a, %d %B, %y %I:%H:%M:%S %p'))
print(n.strftime('%A, %d %B, %y %I:%H:%M:%S %p'))
'''
#specfic date to mention timedelta
'''
from datetime import date,time,datetime,timedelta
n=datetime.now()
n15=n+timedelta(minutes=15)
n2=n+timedelta(days=2)
n7=n+timedelta(days=7)

print(n15,n2,n7,sep='\n')

'''































