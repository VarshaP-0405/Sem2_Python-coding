password=input("Enter the password:")
result=" "
for char in password:
 if char.isdigit():
 break
 result+=char
print("Your output will Break here - ",result)
password=input("Enter your password:")
result=" "
for char in password:
 if not char.isdigit():
 result+=char
print("Your output will continue here - ",result)
