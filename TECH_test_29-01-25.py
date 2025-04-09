class Pizza_Size:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def check_budget(self,budget):
        try:
            if not(isinstance(budget,(int,float))) or budget<0:
                raise ValueError("budget should be integer or float,and should not be negative")
            return True
        except ValueError as ve:
            print(ve)
    def calculate_balance(self,budget):
        return budget-self.price
    def suggest_pizza(self,budget):
        try:
            self.check_budget(budget)
            if budget>self.price:
                print("You Can buy",self.name,"pizza")
                print(f"The balance is: {self.calculate_balance(budget)}")
            elif budget==self.price:
                print("You Can buy",self.name,"pizza")
                print("no balance is remaining")
            else:
                print("sorry you cannot buy pizza")
                print(f"you need {self.price} to buy{self.name} pizza")
        except ValueError as ve:
            print(ve)
small=Pizza_Size("small",200)
medium=Pizza_Size("medium",300)
large=Pizza_Size("large",500)
choice=[small,medium,large]
budget=float(input("enter your budget"))
try :
    for ch in choice:
        ch.suggest_pizza(budget)
except ValueError:
    print("enter numerical values only")
    
            
            
