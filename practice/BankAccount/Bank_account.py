class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, accuntName):
        self.balance = initialAmount
        self.name = accuntName
        print(f"Welcome {self.name}! your account is created.")

    def get_balance (self):
        print(f"Dear {self.name}, your balance is ${self.balance: .2f}\n")
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.get_balance()
        print("\nDeposit Compeleted!")

    
    def check_transaction(self, amount):
        if self.balance >= amount :
            return
        else:
            raise BalanceException (f"Sorry {self.name}, your account only has ${self.balance} of balance")
    
    def withdraw(self, amount):
        try:
          self.check_transaction(amount)
          self.balance = self.balance - amount
          print("\nWithdraw Completed!")
          self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw is interrupted: {error}")
    
    def transfer(self, amount, accuntName):
        try:
          print(f"\n***Transfer Started***")
          self.check_transaction(amount)
          self.withdraw(amount)
          accuntName.deposit(amount)
          print(f"***Transfer Compeleted***\n")
        except BalanceException as error:
            print(f"\nWithdraw is interrupted: {error}")

class IntrestRewardAccount(BankAccount):
    def deposit(self, amount):
        self.balance +=( amount * 1.05)
        print("Deposit completed.\n")
        self.get_balance()
        
class FeeAccount(IntrestRewardAccount):
    def __init__(self , initalAmount , actName ):
        super().__init__(initalAmount , actName)
        self.fee = 5

    def transfer(self, amount, accName):
        try:
            print("\n***Transfer started***")            
            self.check_transaction(amount + self.fee)
            self.withdraw(amount + self.fee)
            accName.deposit(amount)
            print("***Transfer compeleted***")            
        except BalanceException as error:
            print(f"\nTransfer intrrupted : {error}")





        

