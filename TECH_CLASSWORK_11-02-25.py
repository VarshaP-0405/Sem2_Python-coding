def hollow_pyramid(n):
    for i in range(1,n+1):
        space=" "*(n-i)
        if i==1:
            print(space+"*")
        elif i==n:
            print("*"*(2*n-4))
        else:
            middle_space=" "*(2*i-3)
            print(space+"*"+middle_space+"*")
num=int(input())
hollow_pyramid(num)
