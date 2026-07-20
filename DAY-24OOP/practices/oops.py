'''
#Define a class

class person:
    def __init__(self,name,age): #constructor
        self.name=name
        self.age=age
        
    def introduce(self):    #method
        print (f"I am {self.name} and I am {self.age} years old")

#creates objects      
p1=person("ashu",21)
p2=person("chtkii",22)

#call method
p1.introduce()
p2.introduce()
              
'''

class bike:
    brand="RE"

    def start(self):
        print("Bike started")
b1 = bike()
print(b1.brand)

b1.start()
    
    
