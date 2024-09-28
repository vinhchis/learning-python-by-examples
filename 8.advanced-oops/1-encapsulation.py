class BankAccount: 
    def __init__(self, account_number, balance): 
        self.__account_number = account_number   # Private attribute 
        self.__balance = balance  # Private attribute 

    def get_balance(self): 
        return self.__balance 
 
    def deposit(self, amount): 
        if amount > 0: 
            self.__balance += amount 
 
    def withdraw(self, amount): 
        if 0 < amount <= self.__balance: 
            self.__balance -= amount 
 
# Create an instance of the BankAccount class 
account = BankAccount("123456", 1000) 
 
# Accessing attributes indirectly through methods 
print("Initial Balance:", account.get_balance()) 
account.deposit(500) 
account.withdraw(300) 
print("Final Balance:", account.get_balance()) 
# print(account.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'