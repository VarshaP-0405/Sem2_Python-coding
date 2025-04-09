#SyntaX for lambda
#lambda arguements:eXpression
#3 Variables
add=lambda a,b,c:a+b+c
print(add(1,2,3))
#2 Variables
sub=lambda d,e:d-e
print(sub(56,6))
#Square Each value in list
L1=list(map(int,input().split()))
square=map(lambda v:v**2,L1)
print(list(square))
#filter even numbers in a list
L2=list(map(int,input().split()))
even=filter(lambda v:v%2==0,L2)
print(list(even))
#list1--employee name list2--employee salary list3--phone number sort list2 and the names in list 1 should be sorted accordingly
L1=input().split()
L2=list(map(int,input("enter values for employee salary").split()))
L3=list(map(int,input("enter values for employee phone number").split()))
res=list(zip(L2,L1))
print("original list:",res)
res2=sorted(res)
print("sorted list:",res)
print(res2)
lis=list(zip(L1,L2,L3))
res_1=sorted(lis,key=lambda  v:v[1])
print(res_1)
