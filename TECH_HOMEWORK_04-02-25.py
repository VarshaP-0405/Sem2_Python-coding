def lenword(s):
    words = s.strip().split()
    return len(words[-1])
str1=input("enter your string")
res=lenword(str1)
print(res)
##2##
a = input("ENTER BINARY VALUE1")
b = input("ENTER BINARY VALUE2")
result = bin(int(a, 2) + int(b, 2))[2:]
print(result)  # Output: "100"
