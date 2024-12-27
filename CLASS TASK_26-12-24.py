STR=input()
ST=""
C=0
while C<len(STR):
    RES=int(STR[C])*STR[C+1]
    C=C+2
    ST=ST+RES
print(ST)
