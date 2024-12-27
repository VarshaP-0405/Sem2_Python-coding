num=int(input("enter a number"))
n1=0
n2=1
count=0
if num<=0:
    print("enter positive integer")
elif num==1:
    print("the fibonniacci series is",n1)
else:
    while count<num:
        print("the fibonniacci series is")
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count+=1
