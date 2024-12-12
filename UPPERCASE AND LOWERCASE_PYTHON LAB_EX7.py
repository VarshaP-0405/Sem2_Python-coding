STR=input("Enter the string")
upp=0
low=0
for i in STR:
    if i.isupper():
        upp+=1
    elif i.islower():
        low+=1
print("The Uppercase letter count is :",upp)
print("The Lowercase letter count is :",low)



