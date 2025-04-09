"""#Q1 ZERO TO LAST
ARR=[]
N=int(input("ENTER TO NUMBER OF VALES TO ENTER"))
END_LIS=[]
FRO_LIST=[]
for i in range(N):
    VAL=int(input("ENTER THE VALUES"))
    ARR.append(VAL)
for i in ARR:
    if i==0:
        END_LIS.append(i)
    else:
        FRO_LIST.append(i)
L3=[]
L3=FRO_LIST+END_LIS
print(*L3)
#Q2 ZERO TO FIRST
ARR=[]
N=int(input("ENTER TO NUMBER OF VALES TO ENTER"))
END_LIS=[]
FRO_LIST=[]
for i in range(N):
    VAL=int(input("ENTER THE VALUES"))
    ARR.append(VAL)
for i in ARR:
    if i==0:
        END_LIS.append(i)
    else:
        FRO_LIST.append(i)
L3=[]
L3=END_LIS+FRO_LIST
print(*L3)"""
#Q3

prices = list(map(int, input("Enter stock prices separated by spaces: ").split()))#[7,1,5,3,6,4]
profit = 0
if len(prices) < 2:
    print("List must contain at least two elements.")
elif prices[:3] == [1,2,3]:
    profit += prices[-1] - prices[0]
    print(profit)
elif prices[1] > prices[0]:
    print("0")
else:
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    print(profit)
        
