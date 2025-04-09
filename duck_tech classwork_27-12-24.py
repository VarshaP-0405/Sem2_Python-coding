class CreditCardPayment:
    def pay(self,amount):
        return f"paid {amount} using creditcard"
class PayPalPayment:
    def pay(self,amount):
        return f"paid {amount} using PayPal"
class DebitCardPayment:
    def pay(self,amount):
        return f"paid {amount} using debitcard"

def process_payment(payment_method,amount):
    print(payment_method.pay(amount))

cc=CreditCardPayment()
process_payment(cc,200)

pp=PayPalPayment()
process_payment(pp,500)

dc=DebitCardPayment()
process_payment(dc,800)
