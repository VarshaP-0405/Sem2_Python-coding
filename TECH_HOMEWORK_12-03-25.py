N=int(input())
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j == i or j == (N - i + 1): 
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print() 

