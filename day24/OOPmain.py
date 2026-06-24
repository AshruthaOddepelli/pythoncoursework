#class-> blueprint
#attribute->variable-> value
#{2type}-class-Instance
#method->function->action
#{3type}-class-Instance-static
#object->instance of class

class Flipkart:
    discount= 10
    product =['laptop','phone','mouse','charger']

    @classmethod
    def showproduct(cls):
        print(cls.product)

    def login(self,username,password):
        self.username = username
        self.password = password
        print(f'welcome to the flipkart {self.username}')

    @staticmethod
    def banner():
        print("10% discount is going on flipkart, shop now!")
    
pranathi = Flipkart()
pranathi.login('pranathi','pranthi@123')
pranathi.banner()
pranathi.showproduct()
