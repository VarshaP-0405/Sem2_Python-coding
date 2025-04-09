LIST= list(map(int, input("Enter stock prices separated by spaces: ").split()))
C=0
for i in range(1,len(LIST)):
    if (LIST[i])==0:
        print(LIST[i])
        C+=1
        LIST.pop(LIST[i])
print(LIST)
for i in range(C):
    LIST.append(0)
print(LIST)
