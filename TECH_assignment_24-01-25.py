#1
first_name=input("Enter the first name:") 
last_name=input("Enterr the last name:") 
fullname=first_name+last_name 
print("Your name is:",fullname) 
clg=input("Enter the college name:") 
dept=input("Enter the department name:") 
print("Your college name is :",clg+" "+dept)
phone_no=input("Enter the mobile number:") 
ascii_name=[] 
for i in name:
    if i!="":
        ascii_name.append(ord(i)) 
print(f"Your ASCII name is :{i}-{ord(i)}") 
ascii_mobile=[] 
for i in phone_no:
    if i!="":
        ascii_no=ord(i)
        ascii_mobile.append(ascii_no) 
print(f"Your ascii mobile number is:{i}-{ascii_no}") 
for i in range(len(ascii_name)):
    for j in range(len(ascii_mobile)):
        if i==j:
            print(ascii_name[i]+ascii_mobile[j])
#2
p = int(input("Enter the first value: ")) 
q = int(input("Enter the second value: ")) 
r = int(input("Enter the third value: ")) 

add = p +q
sub= p - q
mul=p * q
div= p/q 
 print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")

print("\nBefore Swapping:")
print(f"First value: {p}")
print(f"Second value: {q}")
print(f"Third value: {r}")
p = r
q=p
r=q
print("\nAfter Swapping:")
print(f"First value: {p}")
print(f"Second value: {q}")
print(f"Third value: {r}")
#3
username=input("Enter first name:") 
filtered_name="" 
for char in username:
    if not char.isdigit():
        filtered_name+=char 
print("Hi!!! Your entered input is:",filtered_name) 
print() 
username=input("Enter first name:") 
characters="" 
spl_chars="" 
for char in username:
    if char.isalpha():
        characters+=char
    elif not char.isdigit():
        spl_chars+=char 
print("Your entered characters are:",characters) 
print("Your entered special characters are:",spl_chars)
