class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.max_withdraw = 1000
        self.min_withdraw = 100000
    
    def getBalance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount > 0 :
            self.balance+=amount
            print(f'Successfully deposit {amount} taka')
        else:
            print('Must have to enter positive number')
    
    def withdraw(self,amount):
        if self.max_withdraw < amount :
            print(f'You can not withdraw more than {self.max_withdraw}')
        elif self.balance<amount:
            print(f'Tomar bank e {amount} taka nai')
        else:
            self.balance-=amount
            print(f'Successfully withdrawn {amount} taka')


mamar_bank = Bank(1000)

mamar_bank.deposit(100)

mamar_bank_balance = mamar_bank.getBalance()
print(mamar_bank_balance)

mamar_bank.withdraw(25)

