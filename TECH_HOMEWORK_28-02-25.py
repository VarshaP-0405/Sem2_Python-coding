##1##
n=int(input())
V=97
L=[]
for i in range(n):
    st=""
    st+=chr(V)
    st+=chr(V+1)
    st+=chr(V)
    st+=chr(V+1)
    L.append(st)
    V+=1
for i in L:
    print(i)
##2##
n=int(input())
V=97
L=[]
for i in range(n):
    st=""
    st+=chr(V)
    st+=chr(V)
    st+=chr(V+1)
    st+=chr(V+1)
    L.append(st)
    V+=1
for i in L:
    print(i)
