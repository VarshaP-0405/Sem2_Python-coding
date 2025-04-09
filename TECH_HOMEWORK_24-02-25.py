"""start = int(input("ENTER START: "))  
end = int(input("ENTER END: "))  
L = [2, 3, 5, 7]  
L1 = []  

for i in range(start, end + 1):  
    if i in L:  
        L1.append(i)  
    else:
        is_prime = True
        for j in L:
            if i % j == 0:
                is_prime = False
                break
        if is_prime and i > 1:
            L1.append(i)  

for v in range(len(L1) - 1):  
    if L1[v + 1] - L1[v] == 2:  
        print((L1[v], L1[v + 1]))  """
##2##
start = int(input("ENTER START: "))  
end = int(input("ENTER END: "))  
L1 = []  

for i in range(start, end + 1):  
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1): 
        if i % j == 0:
            is_prime = False
            break
    if is_prime and i > 1:
        if str(i) == str(i)[::-1]:
            print(i)

