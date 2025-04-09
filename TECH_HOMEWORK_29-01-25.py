def longest_good_subarray(nums):
    prefix_sum = 0
    index_map = {0: -1}  
    max_length = 0

    for i, num in enumerate(nums):
        prefix_sum += 1 if num == 1 else -1  

        if prefix_sum in index_map:
            max_length = max(max_length, i - index_map[prefix_sum])
        else:
            index_map[prefix_sum] = i  

    return max_length

array=list(map(int,input("enter an array").split()))
print(longest_good_subarray(array))
##2##
class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display_customer(self):
        print(f"Customer Name : {self.name}")
        print(f"Customer Phone No. : {self.phone}")

class Depositor(Customer):
    def __init__(self, name, phone, accno, balance):
        super().__init__(name, phone)
        self.accno = accno
        self.balance = balance

    def display_depositor(self):
        self.display_customer()
        print(f"Customer A/C No. : {self.accno}")
        print(f"Balance : {self.balance}")

class Borrower(Depositor):
    def __init__(self, name, phone, accno, balance, loan_no, loan_amt):
        super().__init__(name, phone, accno, balance)
        self.loan_no = loan_no
        self.loan_amt = loan_amt

    def display_borrower(self):
        self.display_depositor()
        print(f"Loan No. : {self.loan_no}")
        print(f"Loan Amount : {self.loan_amt}")
        print("--------------------------------------------------")


n = int(input("Enter number of customer details you want to add : "))
customers = []


for _ in range(n):
    name = input("Enter Customer Name : ")
    phone = input("Enter Customer Phone.No : ")
    accno = input("Enter Customer A/C No : ")
    balance = float(input("Enter Balance : "))
    loan_no = input("Enter Loan number : ")
    loan_amt = float(input("Enter Loan Amount : "))
    
    customer = Borrower(name, phone, accno, balance, loan_no, loan_amt)
    customers.append(customer)
    print("***********************************************")


for customer in customers:
    customer.display_borrower()

