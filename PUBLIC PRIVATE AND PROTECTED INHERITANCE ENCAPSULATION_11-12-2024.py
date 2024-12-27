"""#1
class Student:
    id=int(input("ENTER THE USER ID"))#PUBLIC VARIABLE CALLED OUTSIDE SO CANNOT SEE THE VALUES 
    __age=int(input("ENTER THE USER AGE"))#PRIVATE
    
    def __init__(self,name):
        self.__name=name#PRIVATE CALLED INSIDE DEF SO THE VALUE WILL BE DISPLAYED 
    def display(self):
        print("Name=",self.__name)
s=Student("Ria")
s.display()
print(s.id)
print(s.__age)"""
#2
#OTHER METHOD TO SEE THE VALUES OF PRIVATE VARIABLE
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
NAME=input("Enter your name")
SALARY=int(input("Enter the salary"))
emp=Employee(NAME,SALARY)
print("The name is :",emp.name)
print("The salary of the employee is:",emp._Employee__salary)
#3
#OTHER METHOD TO SEE THE VALUES OF PRIVATE VARIABLE#ALSO USING INHERITANCE
class Teacher:
    def __init__(self,tname):
        self.tname=tname
class Student(Teacher):
     def __init__(self,tname,stu_Id,stu_Name):
        super().__init__(tname)
        self.__stu_Id=stu_Id
        self.stu_Name=stu_Name
stu=Student("Bargavi",50,"Varsha")
print("The Name of the Teacher is:",stu.tname)
print("The Student id is :",stu._Student__stu_Id)
print("The Student Name is:",stu.stu_Name)













