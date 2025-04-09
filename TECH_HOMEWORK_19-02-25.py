class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")

methods = [CreditCard(), PayPal(), UPI()]
for method in methods:
    method.pay(500)
##2##
l=list(map(int,input("enter values to enter in list").split()))
seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1
