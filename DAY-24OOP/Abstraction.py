from abc import ABC, abstractmethod

class BankAccount(ABC):
    def checkbalance(self):
        print("you can checkout your balance")
    def Viewhistory(self):
        print("you can checkout your transaction")   
    def userinfo(self):
        print("you can see your details")
    def transaction(self):
        print("you can transfer money through netbanking")
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class CurrentAccount(BankAccount):
    def deposit(self):
        print("you can deposit - CA ")
    def withdraw(self):
        print("You can withdraw - CA")
        
class SavingAccount(BankAccount):
    def deposit(self):
        print("you can deposit - SA ")
    def withdraw(self):
        print("You can withdraw - SA")
        
class ZeroBalanceAccount(BankAccount):
    def deposit(self):
        print("you can deposit - ZBA ")
    def withdraw(self):
        print("You can withdraw - ZBA")
        
class FixedDeposit(BankAccount):
    def deposit(self):
        print("you can deposit - FD ")
    def withdraw(self):
        print("You can withdraw - FD")
        
class SalaryAccount(BankAccount):
    def deposit(self):
        print("you can deposit - SSA ")
    def withdraw(self):
        print("You can withdraw - SSA")

ashrutha=ZeroBalanceAccount()
ashrutha.deposit()
ashrutha.withdraw()
ashrutha.checkbalance()
ashrutha.Viewhistory()
ashrutha.userinfo()
ashrutha.transaction()

ashu=FixedDeposit()
ashu.deposit()
ashu.withdraw()
ashu.checkbalance()
ashu.Viewhistory()
ashu.userinfo()
ashu.transaction()

ashritha=SalaryAccount()
ashritha.deposit()
ashritha.withdraw()
ashritha.checkbalance()
ashritha.Viewhistory()
ashritha.userinfo()
ashritha.transaction()





