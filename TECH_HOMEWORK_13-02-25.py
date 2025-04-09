##1##
def Pattern(N):
    for i in range(1,N+1):
        print(" " * (N - i), end="")
        for j in range(1,i+1):
            print(j,end=' ')
        print()
N=int(input("enter a value:"))
Pattern(N)
##2##
def Prime_check(n,l=[2,3,5,7]):
    if n in l:
        return True
    for i in l:
        if n%i==0:
            return False
        else:
             return True
n=int(input("enter a number to check for prime"))
res=Prime_check(n)
if res==True:
    print(n,"is a prime number")
else:
    print(n,"is  not a prime number")
