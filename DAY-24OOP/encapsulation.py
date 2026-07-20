#mean restrict data
#username can modify
#private instagram method  __password variable
#public password mean 
# protect _
#public _ _
'''
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
'''
#another security of the date -> encapsulation
'''
class Instagram:
    def __init__(self):
        self._post=[]
    
    @property
    def accesspost(self):
        return self._post
    
    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)
        
ashrutha=Instagram()
print(dinesh.accesspost)
ashrutha.accesspost='class and object'
print(dinesh.accesspost)
'''
def pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end=" ")
    print( )
pattern(5)