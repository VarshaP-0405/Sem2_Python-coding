class Calculator:
    def calc(self,a,b=0,c=0):
        if a!=int(a) and b!=int(a) and c!=int(a):
            print("Value Error")
        else:
            if a!=0 and b==0 and c==0:
                res=a*a
                return res
            elif a!=0 and b!=0 and c==0:
                res=a+b
                return res
            elif a!=0 and b!=0 and c!=0:
                res=a*b*c
                return res
s=Calculator()
result=s.calc(5)
print("The Square is:",result)
result=s.calc(5,6)
print("The Sum is:",result)
result=s.calc(5,4,3)
print("The Product is:",result)
