class User:
    def __init__(self, name, dpt, pwd, repwd):
        self.name = name
        self.dpt = dpt
        self.pwd = pwd
        self.repwd = repwd

    def disp_det(self):
        print("Your Encoded Name is:")
        for _ in range(len(self.name)):
            print("X", end="")
        print(" – Fresher")
        
        print("Your Department is:")
        for _ in range(len(self.dpt)):
            print("X", end="")
        print()
        
        print("Your Password is:")
        for _ in range(len(self.pwd)):
            print("X", end="")
        print()
        
        print("Re-Type your Password:")
        for _ in range(len(self.repwd)):
            print("X", end="")
        print()



special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

while True:
    name = input("ENTER NAME: ")
    if not name.isalpha(): 
        print("Invalid name. The name should contain only alphabets. Please try again.")
        continue  
    else:
        break

while True:
    pwd = input("ENTER PASSWORD: ")
    repwd = input("RETYPE SAME PASSWORD: ")

    if any(char in special_chars for char in pwd) and pwd == repwd:
        break
    else:
        print("Invalid password. Ensure it has at least one special character and both passwords match. Please try again.")


dpt = input("ENTER DEPARTMENT: ")


res = User(name, dpt, pwd, repwd)
res.disp_det()
##2##
n=list(map(int,input("enter a list ").split()))
val=int(input("enter the element to remove"))
print("the existing list is:",n)
for i in n:
    if i==val:
        n.remove(i)
        break
print("the new list is ",n)
##3##
arr=[]
n=int(input("enter the number of elements "))
for i in range(n):
    val=input("enter value")
    arr.append(val)
print("your non inverse order array is:",arr)
inverse_arr=list(reversed(arr))
print("your inverse order array is:",inverse_arr)
