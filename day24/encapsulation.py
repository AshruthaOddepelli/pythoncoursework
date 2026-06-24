#mean restrict data
#username can modify
#private instagram method  __password variable
#public password mean 
class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self.followers = []
       


    
    def getpassword(self):
        return self.__password
    
    def setpassword(self,newpassword):
        self.__password = newpassword

        print(f'welcome to the Instagram, {self.username}')
vamsi = Instagram('vamsi','vamsi@123')

print("Before username:",vamsi.username)
vamsi.username='Ashrutha'
print("After username:",vamsi.username)

print("Before password :",vamsi.getpassword())
vamsi.setpassword('Ashrutha@123')
print("After password:",vamsi.getpassword())
