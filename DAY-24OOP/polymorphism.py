#method overriding->same method and same parameter but different cls
'''

class Hotstar:
    def __init__(self,name):
        self.name=name
        print(f"hi {self.name},welcome to the Hotstar")
    def login(self):
        print("You can login")
    def dashboard(self):
        print("You can see the dashboard items")
    def sreach(self):
        print("You can sreach")
    def languages(self):
        print("You can select the login")
    def playcontroller(self):
        print("You can play,pause and speed1X,2X")
    def ads(self):
        print("You can see many ads")
    def movies(self):
        print("You can see limited movies")
    def sports(self):
        print("You can see limited time to watch")
    def quality(self):
        print("limited quality")

class PremiumHotstar(Hotstar):
    def __init__(self,name):
        self.name=name
        print(f"hi {self.name},welcome to the PremiumHotstar")
    def ads(self):
        print("ads won't run")
    def movies(self):
        print("You can see unlimited movies")
    def sports(self):
        print("You can watch sport")
    def quality(self):
        print("high quality")
    

subbu=Hotstar('subbu')
subbu.login()
subbu.dashboard()
subbu.sreach()
subbu.languages()
subbu.playcontroller()
subbu.ads()
subbu.movies()
subbu.sports()
subbu.quality()

ashru=PremiumHotstar('ashrutha')
ashru.login()
ashru.dashboard()
ashru.sreach()
ashru.languages()
ashru.playcontroller()
ashru.ads()
ashru.movies()
ashru.sports()
ashru.quality()

'''
#operation overloading->operation can lead with overloading

class Number:
    def __init__(self,n):
        self.n = n
    def __add__(self,other):
        return self.n + other.n
    def __sub__(self,other):
        return self.n - other.n
    def __mul__(self,other):
        return self.n * other.n
    def __truediv__(self,other):
        return self.n / other.n
    def __eq__(self,other):
        return self.n == other.n
    def __lt__(self,other):
        return self.n < other.n
    def __gt__(self,other):
        return self.n > other.n
    def __str__(self):
        return str(self.n)

n1=Number(10)
n2=Number(20)

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1==n2)
print(n1<n2)
print(n1>n2)
print(n1,n2)



































