class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def add_interest(self, rate):
        if rate > 0:
            interest = self.__balance * rate / 100
            self.__balance += interest
            print(f"Added interest: ${interest}. New balance: ${self.__balance}")
        else:
            print("Interest rate must be positive.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number


account = BankAccount("1234567890", 1000)
val=int(input("enter the value to deposit")
account.deposit(val)
val_with=int(input("enter the value to deposit")
account.withdraw(val_with)
val_intre=int(input("enter your intrest value"))
account.add_interest(val_intre)                  
print(f"Final balance: ${account.get_balance()}")  
