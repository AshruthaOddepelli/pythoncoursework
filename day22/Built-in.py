#cmd ,files located,version,exit
'''
import sys
print(sys.argv)#for cmd catch the file
print(sys.path)#packages where files located
print(sys.version)#what version my using
print("Before exit")
sys.exit()#exit from 
print("After exit")
'''
#Windows 10 Intel64 Family 6 Model 186 Stepping 3, GenuineIntel
'''
import platform
print(platform.system(),platform.release(),platform.processor())

'''

#math function
'''
import math

print(math.pi)#3.141592653589793

print(math.e)#2.718281828459045

print(math.sqrt(25))#5
print(math.pow(2,5))#32

print(round(20.3))#20
print(round(20.8))#21
print(round(20.5))#20

print(math.ceil(12.3))#13
print(math.ceil(12.000001))#13
print(math.ceil(12.8))#13
print(math.ceil(12.99999))#13

print(math.floor(12.99999))#12
print(math.floor(12.00001))#12
print(math.floor(12.3))#12
print(math.floor(12.8))#12

print(math.fabs(-12))
print(math.factorial(5))
print(math.gcd(8,28))#greates common divisor

print(math.log(10,10))
print(math.sin(10))
print(math.cos(10))
print(math.tan(10))

print(math.degrees(20))
print(math.radians(20))

'''
#random

import random

random.seed(4)
print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))

l=['python','java','c++','HTMl','SQL']
print(random.choice(l))
print(random.choices(l,k=3))

s='rps'
print(random.choice(s))
print(l)
random.shuffle(l)
print(l)






























