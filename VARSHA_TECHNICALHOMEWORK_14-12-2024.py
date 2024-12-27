"""#Question1
st1=input("enter string 1")
st2=input("enter string 2")
con_str=[]
n1=len(st1)
n2=len(st2)
i=0
j=0
while i<n1 and j<n2:
        con_str.append(st1[i])
        con_str.append(st2[j])
        i+=1
        j+=1
if i<n1:
    con_str.append(st1[i:])
if j<n2:
    con_str.append(st1[j:])
print(' '.join(con_str))"""
#Question2
flowerbed = list(map(int, input("Enter the flowerbed as space-separated values (0 for empty, 1 for planted): ").split()))
n = int(input("Enter the number of flowers to plant: "))
count = 0  
length = len(flowerbed)  
i = 0
while i < length:
    if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
        flowerbed[i] = 1  
        count += 1
        i += 1 
    if count >= n:  
        print(True)
        break
    i += 1
if count < n:  
    print(False)

        
