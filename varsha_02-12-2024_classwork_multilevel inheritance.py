"""class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("The Name is:",self.name,"\nThe Age is:",self.age)
class Employee(Person):
    def __init__(self,name,age,Id):
        super().__init__(name,age)
        self.Id=Id
    def display(self):
        self.show()
        print("The Id is:",self.Id)
class Manager(Employee):
    def __init__(self,name,age,Id,salary):
        super().__init__(name,age,Id)
        self.salary=salary
    def display_man(self):
        self.display()
        print("The Salary is:",self.salary)
name=input()
age=int(input())
Id=int(input())
salary=int(input())
M=Manager(name,age,Id,salary)
M.display_man()"""

#2
class Teacher:
    def __init__(self,name,sub):
        self.name=name
        self.sub=sub
    def show(self):
        print("The Teacher Name is:",self.name,"\nThe Subject is:",self.sub)
class Student1(Teacher):
    def __init__(self,name,sub,stu_Id,stu_Name):
        super().__init__(name,sub)
        self.stu_Id=stu_Id
        self.stu_Name=stu_Name
    def display_stu1(self):
        self.show()
        print("The First Student Id is:",self.stu_Id,"The First Student Name is:",self.stu_Name)
class Student2(Teacher):
    def __init__(self,name,sub,stu_Id,stu_Name):
        super().__init__(name,sub)
        self.stu_Id=stu_Id
        self.stu_Name=stu_Name
    def display_stu2(self):
        self.show()
        print("The Second Student Id is:",self.stu_Id,"The Second Student Name is:",self.stu_Name)
class Student3(Teacher):
    def __init__(self,name,sub,stu_Id,stu_Name):
        super().__init__(name,sub)
        self.stu_Id=stu_Id
        self.stu_Name=stu_Name
    def display_stu3(self):
        self.show()
        print("The Third Student Id is:",self.stu_Id,"TheThird Student Name is:",self.stu_Name)
name=input("Enter Teacher name")
sub=(input("Enter the subject teacher is teaching" ))

stu_Id1=int(input("Enter the first student id"))
stu_Name1=(input("Enter the first student name"))
stu1=Student1(name,sub,stu_Id1,stu_Name1)
stu1.display_stu1()

stu_Id2=int(input("Enter the second student id"))
stu_Name2=(input("Enter the second student name"))
stu2=Student2(name,sub,stu_Id2,stu_Name2)
stu2.display_stu2()

stu_Id3=int(input("Enter the third student id"))
stu_Name3=(input("Enter the third student name"))
stu3=Student3(name,sub,stu_Id3,stu_Name3)
stu3.display_stu3()

    
