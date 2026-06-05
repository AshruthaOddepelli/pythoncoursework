data = ('abc','1234')

username,password =input("enter the username and password:").split()

if data == (username,password):
    print("login succesfull")
else:
    print("Invalid login")
