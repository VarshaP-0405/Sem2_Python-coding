#Question 1#
Name=input()
Roll_No=int(input())
a=int(input("Enter the marks obtained in subject 1"))
b=int(input("Enter the marks obtained in subject 2"))
c=int(input("Enter the marks obtained in subject 3"))
d=int(input("Enter the marks obtained in subject 4"))
e=int(input("Enter the marks obtained in subject 3"))
tot=a+b+c
per=(tot/300)*100
if per>=85:
    print("Grade S")
elif per>=75 and per<=85:
    print("Grade A")
elif per>=65and per<=75:
    print("Grade B")
elif per>=55and per<=65:
    print("grade C")
elif per>=50 and per>=55:
    print("Grade D")
#Question 2#
class StudentInfo:
 def __init__(self,name,age,course,grade):
 self.name=name
 self.age=age
 self.course=course
 self.grade=grade
 def display(self):
 print("Student name is",self.name)
 print("Student age is",{self.age})
 print("Student course is",self.course})
 print("Student grade is",{self.grade})
 def __del__(self):
     print("Student's detail is deleted")
info=StudentInfo("Varsha",18,"BSc with AI","A+")
info.display()
info.__del__()
