sentence=input("enter a sentence")
words=sentence.split()
for i in range(len(words)) :
    if i%2!=0:
        words[i]=words[i][::-1]
res=" ".join(words)
print(res)
