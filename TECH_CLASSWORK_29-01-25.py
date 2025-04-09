class Maggi_Pack:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def check_budget(self,budget):
        if not(isinstance(budget,(int,float))) or budget<0:
            raise ValueError("Budget cannot be negative")
        return True
    def calculate_balance(self,budget):
        return budget-self.price
    def suggest_packs(self,budget):
        try:
            self.check_budget(budget)
            if budget>self.price:
                print("you can buy",self.name,"pack")
                print(f"Your remaining balance is:{self.calculate_balance(budget)}")
            elif budget==self.price:
                print("you can buy",self.name,"pack.No balance is remaining")
            else:
                print(f"You will not be able to afford it.You will need {self.price}to buy {self.name} pack")
        except ValueError as ve:
            print(ve)
            
small=Maggi_Pack("small",20)
regular=Maggi_Pack("regular",30)
big=Maggi_Pack("big",50)
packets=[small,regular,big]

budget=float(input("enter the budget"))
try:
    for i in packets:
        i.suggest_packs(budget)
except ValueError:
    print("Enter a numerical value only!!")



