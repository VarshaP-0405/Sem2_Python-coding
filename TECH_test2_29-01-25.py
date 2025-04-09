n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()

DICT1={}
n=int(input())
for i in range(n):
    key=input()
    val=int(input())
    DICT1[key]=val
print(sum(DICT1.values()))
