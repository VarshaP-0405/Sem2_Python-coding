##1##
def Rev_str(string):
    if len(string)<=1:
        return string
    else:
        return Rev_str(string[1:])+string[0]
string=input("enter your string")
res=Rev_str(string)
print("the original string is:",string,"the reversed string is:",res)
##2##
def Rev_str(string):
    if len(string)<=1:
        return string
    else:
        return Rev_str(string[1:])+string[0]
string=input("enter your string")
res=Rev_str(string)
print("the original string is:",string,"the reversed string is:",res)
if string==res:
    print("the string is pallindrome ")
else:
    print("the string is not pallindrome ")
##3##
def power(val,power_val):
    if power_val==0:
       return 1
    else:
        return val*power(val,power_val-1)
val=int(input("enter the value"))
power_val=int(input("enter the power"))
res=power(val,power_val)
print(res)
##4##
def Sum_str(string):
    sum1=0
    if len(string)==0:
        return 0
    return int(string[0])+Sum_str(string[1:])
string=input("enter your string")
if string.isdigit():
    res=Sum_str(string)
    print("the original string is:",string,"the sum is:",res)
else:
    print("the string should only contain integer and not string")
##5##
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
array = []
print("Enter the elements row by row:")
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1} elements separated by space: ").split()))
    while len(row) != cols:  
        print(f"Error: Please enter exactly {cols} numbers.")
        row = list(map(int, input(f"Re-enter row {i + 1} elements separated by space: ").split()))
    array.append(row)
total_sum = 0
for row in array:
    total_sum += sum(row)
print("\nThe 2D array is:")
for row in array:
    print(row)
print(f"The sum of all elements in the 2D array is: {total_sum}")       
##6##
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
print("Enter the matrix row by row (space-separated):")
for i in range(rows):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    while len(row) != cols:  
        print(f"Error: Please enter exactly {cols} elements.")
        row = list(map(int, input(f"Re-enter row {i + 1}: ").split()))
    matrix.append(row)
print("\nOriginal Matrix:")
for row in matrix:
    print(" ".join(map(str, row)))
transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
print("\nTranspose of the Matrix:")
for row in transpose:
    print(" ".join(map(str, row)))

