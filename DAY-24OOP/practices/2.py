class amazon:
    discount = 20
    product=['Traditional dress','western tops','lehenga','kutis']

    @classmethod
    def showproduct(cls):
        print(cls.product)

    def login(self,username,password):
        self.username = username
        self.password = password
        print(f'welcome to amazon {self.username}')

    @staticmethod
    def banner():
        print("20% discount is going on amazon")
ashu=amazon()
ashu.login('ashrutha','Ashr@123')
amazon.banner()
amazon.showproduct()
    
