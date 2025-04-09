"""x = input()
y = input()
z = input()
flag = False  

for i in x:
    if i in y and i in z:  
        print(i, end="")
        flag = True  

if not flag:
    print(" no common prefix") """

##2##
s = input()
t = input()

i, j = 0, 0  

while i < len(s) and j < len(t):
    if s[i] == t[j]:  
        i += 1
    j += 1  

print(i == len(s))  





          
