##1##
ARR = list(map(int, input("Enter numbers separated by spaces: ").split()))#[1,2,4,5]
NUM = []
for i in range(1,len(ARR)):
    NUM.append(i)

for i in NUM:
    if i not in ARR:
        print("THE MISSING NUMBER IS",i)
    else:
        print("THE MISSING NUMBER IS",(len(ARR)+1))
##2##
ARR = list(map(int, input("Enter numbers separated by spaces: ").split()))
UNI = []  
DUP = [] 
for i in ARR:
    if i not in UNI:
        UNI.append(i)
    else:
        DUP.append(i)
for j in UNI:
    if j not in DUP:
        print(j)
##3##
ARR = list(map(int, input("Enter numbers separated by spaces: ").split()))
ARR_SOR=sorted(ARR)
if ARR==ARR_SOR:
    print("TRUE")
else:
    print("FALSE")
##4##
ARR = list(map(int, input("Enter numbers separated by spaces: ").split()))
UNI = []  
DUP = [] 
for i in ARR:
    if i not in UNI:
        UNI.append(i)
    else:
        DUP.append(i)
MAX = 0
MAX_VAL = 0
for i in UNI:  
    count = ARR.count(i)  
    if count > MAX:
        MAX = count
        MAX_VAL = i
if MAX > (len(ARR) // 2):
    print(f"The maximum repeated value is: {MAX_VAL}, repeated {MAX} times.")
else:
    print("No majority element found.")
##5##
ARR = list(map(int, input("Enter numbers separated by spaces: ").split()))
n=len(ARR)//2
fro_half=ARR[:n]
bac_half=ARR[n:]
sum1=sum(fro_half)
sum2=sum(bac_half)
print(sum1,sum2)
if sum1==sum2:
    print("True")
else:
    print("False")
##6##
ARR = list(map(int, input("Enter numbers separated by spaces: ").split()))
l=[]
target=int(input("enter your target"))
for i in ARR:
    for j in ARR:
        if i!=j and i<j:
            if i+j==target:
                print((i,j),end=" ")

