'''
try:
    a=int(input("Enter the age:"))
except ValueError:
    print("Enter the age in a digit[0-9] format")
else:
    print("Age:",a)
finally:
    print("ThankYou")
'''
#runtime error many error 
'''
try:
    a=int(input("Enter the age:"))
    print(12/10)
    print(b)
    print(16+'14')
    d={1:3,2:4,3:4,4:5}
    print(d[5])
    l=[1,2,3,4]
    print(l[10])
except ValueError:
    print("Enter the age in a digit[0-9] format")
except ZeroDivisionError:
    print("can't divide with zero")
except NameError:
    print("define the var")
except TypeError:
    print("Add the same datatype")
except KeyError:
    print("key is not present")
except IndexError:
    print("Index is out of range")
else:
    print("Age:",a)
finally:
    print("ThankYou")
'''
#to catch mutiply error on line
'''
try:
    a=int(input("Enter the age:"))
    print(12/10)
    print(b)
    print(16+'14')
    d={1:3,2:4,3:4,4:5}
    print(d[5])
    l=[1,2,3,4]
    print(l[10])

except (ValueError,ZeroDivisionError,NameError,TypeError,KeyError,IndexError) as e:
    print("Error occured:",e)
else:
    print("No Error Occured")
finally:
    print("ThankYou")

'''
#all error should be handle with Exception-type3
'''
try:
    a=int(input("Enter the age:"))
    print(12/10)
    print(b)
    print(16+'14')
    d={1:3,2:4,3:4,4:5}
    print(d[5])
    l=[1,2,3,4]
    print(l[10])

except Exception as e:
    print("Error occured:",e)
else:
    print("No Error Occured")
finally:
    print("ThankYou")

'''

'''
try:
    amount=int(input("Enter amount to withdraw:"))
    if amount < 0:
        raise Exception ("Enter the amount greater than zero")
    
except Exception as e:
    print("Error occured:",e)
else:
    print("No Error Occured")
finally:
    print("ThankYou")

'''







    
