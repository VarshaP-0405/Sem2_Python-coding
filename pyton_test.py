print(ord('a'))
print(ord('A'))
str1 = input("Enter a string: ")
l1 = []
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in str1:
    l1.append(i)
for i in lower:
    for j in range(len(l1)):
        if l1[j] == i:
           l1[j] = chr(ord(l1[j]) - 32)
str1 = ''.join(l1)
print(str1)
