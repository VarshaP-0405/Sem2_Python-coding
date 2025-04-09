"""##1##

char=input("enter the capital letter: ")
if 'A'<=char<='Z':
    c=chr(ord(char)+32)
print(c)
##2##

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
##3##

character=input("enter the character: ")
print("Conversion:",end="")
for i in character:
    if 'A'<=i<='Z':
        x=ord(i)
        y=chr(x+32)
    print(y,end="")"""
##4##
def lowcase(ch):
    p=ord(ch)
    q=chr(p+32)
    print(q,end="")
def uppcase(ch):
    X=ord(ch)
    Y=chr(X-32)
    print(Y,end="")
string1=input()
for i in string1:
    if 'A'<=i<='Z':
        lowcase(i)
    elif 'a'<=i<='z':
        uppcase(i)
