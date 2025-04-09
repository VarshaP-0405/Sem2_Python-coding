my_dict = {'a':1,'b': 2,'c': 3}
total_sum = sum(my_dict.values())
print(total_sum)

n=int(input())
for i in range(1, n+1):
    for j in range(i):
        print(i,end="")
    print()
