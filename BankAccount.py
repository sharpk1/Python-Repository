class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print('A new account is created')
    
    def deposit(self, depositAmount):
        self.balance = self.balance + depositAmount
        print("the new balance is now " + str(self.balance))
    
    def withdraw(self,withdrawAmount):
        
        if withdrawAmount >= self.balance:
            print('Funds unavailable!')
        else:
            self.balance = self.balance - withdrawAmount
            print("The new balance is now " + str(self.balance))
        
    def __str__(self):
        return "Account Owner: " + self.owner + "\nAccount Balance: " + str(self.balance)
    
myaccount = Account('Kush', 1000)
myaccount.balance
print(myaccount)
print('Now depositing $100...')
myaccount.deposit(100)
print('Now withdrawing $50...')
myaccount.withdraw(50)