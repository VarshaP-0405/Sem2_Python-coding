nums = list(map(int, input().split()))
k = int(input())
for i in range(k-1):
    max_num = max(nums)  
    nums.remove(max_num)  
print(max(nums))
##2##
num = int(input())
num_str = str(num)
sum_digits=0
for i in range(len(num_str)):
    sum_digits += int(num_str[i]) ** (i + 1)
if sum_digits == num:
    print(f"{num} is a Disarium number")
else:
    print(f"{num} is not a Disarium number")
