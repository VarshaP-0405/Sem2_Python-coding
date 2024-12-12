#1
str_digits = [] 
str_alpha = [] 
str_special = [] 

string = input("Enter Name: ")

for i in string:
    if i.isalpha():
        str_alpha.append(i)
    elif i.isdigit():
        str_digits.append(i)
    else:
        str_special.append(i)

# Join the lists into strings
alpha_characters = "".join(str_alpha)
digit_characters = "".join(str_digits)
special_characters = "".join(str_special)

print("Your entered alphabetic characters are:", alpha_characters)
print("Your entered numeric characters are:", digit_characters)
print("Your entered special characters are:", special_characters)
#2
str=""
str1=""
string=input("Enter Name:")
for i in string:
    if i.isnum():
        str.append(i)
    else:
        str1.append(i)
print("Hi! Your Entered Input is:",str1())










        
