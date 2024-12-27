def Check(string):
    L=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if string.islower()==True and len(string)==26:
        return True
    else:
        return False
    for i in string:
            if i in L:
                L.pop(i)
    if len(L)==0:
        return True
    
        
    
string=input("enter the string")
check_val=Check(string)
if check_val==True:
    print("It is an panagram")
elif check_val==False:
     print("It is not an panagram")
