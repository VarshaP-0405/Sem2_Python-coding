import random

class Customer:
    def __init__(self, cust_id, name, phone_number):
        self.cust_id = cust_id
        self.name = name
        self.phone_number = phone_number

    
    def gen_rand_id():
        c_id = random.randint(1000, 9999)
        return f"TICK{c_id}"

    
    def verify_customer_id(cust_id):
        if cust_id[:4] == "TICK" and len(cust_id) == 8 and cust_id[4:].isdigit():
            print("The id is verified and is correct")
            return True
        else:
            print("The id is invalid")
            return False

class TicketBooking:
    def __init__(self):
        self.events = {
            "Concert": {"price": 1000, "avail_seats": 500},
            "Movie": {"price": 350, "avail_seats": 360},
            "Drama": {"price": 350, "avail_seats": 222}
        }
        self.booked_tickets = []

    def View_events(self):
        for event, details in self.events.items():
            print(f"{event}: {details['price']} per ticket and {details['avail_seats']} seats are available")
        print("Only Limited Seats are available, Hurry up and Book the Tickets :) :) :)")

    def Book_Tickets(self, event_name, no_of_tickets, customer):
        if event_name in self.events:
            event = self.events[event_name]
            if event['avail_seats'] >= no_of_tickets:
                total_price = event['price'] * no_of_tickets
                event['avail_seats'] -= no_of_tickets
                self.booked_tickets.append({
                    "Customer id:": customer.cust_id,
                    "Event_name": event_name,
                    "No_of_Tickets": no_of_tickets,
                    "Price_Total": total_price
                })
                print("Booking successful!")
            else:
                print("Sorry :( :( Seats Not Available")
        else:
            print("Event Name Not Available :( :(, Check for the event name")

    def View_My_Tickets(self, customer):
        print("**********Ticket Information**********")
        cus_ticket = [t for t in self.booked_tickets if t["Customer id:"] == customer.cust_id]
        if not cus_ticket:
            print("No Tickets booked :( :( :(")
        else:
            for tick in cus_ticket:
                print(f"Event: {tick['Event_name']}, Quantity: {tick['No_of_Tickets']}, Total Cost: {tick['Price_Total']}")

if __name__ == "__main__":
    book = TicketBooking()
    print("*********************Welcome to Ticket Booking Application*********************")
    cust_id = input("Enter customer id: ")

    if Customer.verify_customer_id(cust_id):
        Name = input("Enter your name: ")
        Phone_no = int(input("Enter your phone number: "))
        customer = Customer(cust_id, Name, Phone_no)
        print("Valid :) :) :), View the booking details")
    else:
        print("Invalid :( :( :(, Please Register")
        Name = input("Enter your name: ")
        Phone_no = int(input("Enter your phone number: "))
        cust_id = Customer.gen_rand_id()
        customer = Customer(cust_id, Name, Phone_no)
        print("Your Customer id is:", cust_id)

    Flag = True
    while Flag:
        print("\n**********Booking Info**********")
        print("1. View Events")
        print("2. Book Tickets")
        print("3. View My Tickets")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            book.View_events()
        elif choice == 2:
            event_name = input("Enter The Event Name: ")
            no_of_tickets = int(input("Enter The Number of Tickets Required: "))
            book.Book_Tickets(event_name, no_of_tickets, customer)
        elif choice == 3:
            book.View_My_Tickets(customer)
        elif choice == 4:
            Flag = False
            print("Thank you for using the Ticket Booking Application!")
        else:
            print("Enter choice 1-4 only, invalid choice.")
