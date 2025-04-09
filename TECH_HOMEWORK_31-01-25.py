class BookStall:
    def __init__(self, book_name, customer_id, price):
        self.book_name = book_name
        self.customer_id = customer_id
        self.price = price
        self.discount = 0
        self.discounted_price = 0
    
    def validate_input(self):
        if not self.book_name or not self.customer_id.isdigit() or not self.price.isdigit():
            print("Invalid input! Please make sure the book name is not empty, customer ID and price are valid numbers.")
            return False
        return True

    def calculate_discount(self):
        customer_id = int(self.customer_id)
        if 1 <= customer_id <= 100:
            self.discount = 50
        elif 101 <= customer_id <= 300:
            self.discount = 30
        elif 301 <= customer_id <= 400:
            self.discount = 20
        elif 401 <= customer_id <= 500:
            self.discount = 10
        else:
            self.discount = 0
        
        self.discounted_price = float(self.price) * (1 - self.discount / 100)
    
    def display_info(self):
        if self.validate_input():
            self.calculate_discount()
            print(f"Price of the Book is {self.price} MRP")
            print(f"You are eligible for a discount of {self.discount}%")
            print(f"Your discounted price for the book is {self.discounted_price} MRP")

while True:
        book_name = input("Enter your Book Name: ")
        customer_id = input("Enter your Customer ID: ")
        price = input("Enter the price of the Book: ")
        
        book_stall = BookStall(book_name, customer_id, price)
        book_stall.display_info()
        
        continue_option = input("Do you want to continue? (yes/no): ").lower()
        if continue_option != 'yes':
            break

