'''
def function_nmae(arg):
    #statement
    return
function_name(para)
'''
'''
def wish(name):
    print(f'Welcome to the python course {name}!')

wish('Ashrutha')
wish('chutkii')
wish('komalatha')
wish('subbu')
output:
Welcome to the python course Ashrutha!
Welcome to the python course chutkii!
Welcome to the python course komalatha!
Welcome to the python course subbu!
'''
'''
def iseven(num):
    if num%2==0:
        return f"{num}-Even Number"
    else:
        return f"{num}-Odd Number"

print(iseven(12))
print(iseven(13))

output:
12-Even Number
13-Odd Number
'''
'''
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    return fact
    

num=int(input("enter the number: "))
print("Factorial:",factorial(num))



def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num}-Not prime number"
    return f"{num}-prime number"
num=int(input("Enter the number:"))
print(isprime(num))
'''























