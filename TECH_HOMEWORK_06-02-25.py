string=input("Enter the string")
sub_l=[]
sub=""
for i in range(len(string)):
    for j in range(i,len(string)):
        sub_l.append(string[i:j+1])
print(sub_l)
pali=[]
length=[]

for i in sub_l:
    word=i
    rev=word[::-1]

    if word==rev:
        pali.append(word)
        l=len(word)
        length.append(l)
maxi=max(length)
print(maxi)
for i in sub_l:
    if len(i)==maxi and i in pali:
        print(i)
