"""#Question 1
class Alpha:
    def __init__(self,string):
        self.string=string
    def Check(self):
        al=0
        num=0
        spe=0
        l="`~!@#$%^&*():;,<.>/?'"
        for i in self.string:
            if i.isalpha():
                al+=1
                
            elif i.isdigit():
                num+=1
                
            elif i in l:
                spe+=1
                
        print("Alphabetic Characters:",al)
        print("Numeric Characters:",num)
        print("Special Characters:",spe)
st=input("enter your string")
res=Alpha(st)
res.Check()"""

#Question 2
class Alpha:
    def __init__(self,string):
        self.string=string
    def Count(self):
        al=0
        spe=0
        l="`~!@#$%^&*():;,<.>/?'"
        for i in self.string:
            if i.isalpha():
                al+=1
            elif i in l:
                spe+=1
    
        if al>=1 and spe>=1:
            print("The string contains both alphabets and special characters")
        
       
st=input("enter your string")
res=Alpha(st)
res.Count()








