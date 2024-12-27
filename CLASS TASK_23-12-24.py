class Login:
    def check(self):
        
        username=input("enter username")
        pwd=int(input("enter password"))
        Flag=True
        c=0
        if username=="varshu@2007" and pwd==2007:
            Flag=True
            print("the username and password is correct")
            quit()
        else:
            c+=1
            Flag=False
        if Flag==False and c<=5:
            username=input()
            pwd=int(input())
            if username=="varshu@2007" and pwd==2007:
                Flag=True
                print("the username and password is correct")
                quit()
            else:
                left=5-c
                print("the username or password is incorrect",left,"attempts only left")
                c+=1
        elif Flag==False and c>5:
            print("Account Locked")
        
c=Login()
c.check()
##10##
class Extract:
    def __init__(self,string):
        self.string=string
    def check:
        l=[]
        for i in self.string:
            l.append(i)
        for i in l:
            if i=="#":
                l.pop(i)
        "".join(l)
                
