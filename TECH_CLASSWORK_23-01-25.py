f1=open('File1.txt','r')
f2=open('File2.txt','w')
cont=f1.readlines()
for i in range(0,len(cont)):
    if (i%2==0):
        
        f2.write(cont[i])
    else:
        pass
f2.close()
f2=open('File2.txt','r')
cont1=f2.read()
print(cont1)
f1.close()
f2.close()
