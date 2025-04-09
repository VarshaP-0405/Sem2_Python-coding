arr=list(map(int,input("enter the elements of the array seperated by space:").split()))
print("Elements at odd positions:")
for i in range(len(arr)):
    if i%2!=0:
        print("Index:",i,"Value:",arr[i])
print()

for j in range(len(arr)):
      if j%2==0:
        print("Index:",j,"Value:",arr[j])
