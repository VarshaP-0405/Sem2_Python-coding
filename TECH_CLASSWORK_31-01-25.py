name = input("Enter name: ")
ph_no = input("Enter phone number: ")
dob = input("Enter date of birth: ")
seat_count = int(input("Enter total number of seats: "))

num = [str(i) for i in range(1, 21)]
alpha_fir = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
alpha_sec = ['H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
alpha_eco = ['Y', 'Z']

first_class = [j + i for j in alpha_fir for i in num]
second_class = [j + i for j in alpha_sec for i in num]
economic_class = [j + i for j in alpha_eco for i in num]

fir_price = 200
sec_price = 150
eco_price = 50
GST = 0.18

tot_fir = fir_price + (fir_price * GST)
tot_sec = sec_price + (sec_price * GST)
tot_eco = eco_price + (eco_price * GST)

available_seats = first_class + second_class + economic_class

print("\nAvailable Seats:")
print("First class:", first_class)
print("Second class:", second_class)
print("Economic class:", economic_class)

selected_seats = input("Select your seats (comma-separated): ").split(',')

# Calculate total ticket price
total_price = 0
for seat in selected_seats:
    seat = seat.strip()
    if seat in first_class:
        total_price += tot_fir
    elif seat in second_class:
        total_price += tot_sec
    elif seat in economic_class:
        total_price += tot_eco
    else:
        print(f"Seat {seat} is not available.")

print(f"\nHi {name}..! You have successfully booked {seat_count} tickets. Seats: {', '.join(selected_seats)}.")
print(f"Your total price: Rs.{total_price:.2f}")

snacks_choice = input("Do you want Snacks? (Yes/No): ").strip().lower()

snack_prices = {"Popcorn": 100, "Ice Cream": 80, "Puffs": 60, "Tea": 40, "Soft Drinks": 50}
snack_total = 0

if snacks_choice == "yes":
    print("\nAvailable Snacks:")
    for snack, price in snack_prices.items():
        print(f"{snack} - Rs.{price}")
    
        snack_count = int(input("Enter number of snacks you want: "))
    for _ in range(snack_count):
        snack_name = input("Enter snack name: ").strip()
        if snack_name in snack_prices:
            snack_total += snack_prices[snack_name]
        else:
            print(f"{snack_name} is not available.")
    
    print(f"Your snacks price: Rs.{snack_total}")

total_bill = total_price + snack_total
print(f"Your final total bill: Rs.{total_bill:.2f}")
