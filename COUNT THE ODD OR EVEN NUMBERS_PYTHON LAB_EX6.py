


#COUNT 

def count_odd_even(number):
    odd_count = 0
    even_count = 0
    for num in number:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return odd_count, even_count

n = input("Enter numbers separated by spaces: ")
number = []
for num in n.split():
    number.append(int(num))
    
result = count_odd_even(number)
odd_count, even_count = result

print(f"Odd numbers: {odd_count}")
print(f"Even numbers: {even_count}")
