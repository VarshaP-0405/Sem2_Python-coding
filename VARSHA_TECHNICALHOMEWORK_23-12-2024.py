#2
input_list = [4, 2, 7, 4, 9, 1, 2, 7]
modified_list = sorted(set(input_list), reverse=True)
print("Original list:", input_list)
print("Modified list:", modified_list)
#3
number = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str(abs(number)))
print(f"The sum of the digits of {number} is {sum_of_digits}.")
#4
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = [item for item in list1 if item in list2]
print("List 1:", list1)
print("List 2:", list2)
print("Common elements:", common_elements)
#5
input_string = input("Enter a string: ")
word_count = len(input_string.split())
print(f"The number of words in the string is: {word_count}")
#6
input_list = [4, 2, 7, 1, 9, 3]
for i in range(len(input_list)):
    for j in range(0, len(input_list) - i - 1):
        if input_list[j] > input_list[j + 1]:
            input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
print("Sorted list:", input_list)
#7
class BankAccount:
    def _init_(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: {self.balance}")
account = BankAccount("John Doe", 1000)  # Create account with an initial balance of 1000
account.deposit(500)  # Deposit money
account.withdraw(200)  # Withdraw money
account.check_balance()  # Check balance
account.withdraw(2000)  # Try to withdraw more than available balance
