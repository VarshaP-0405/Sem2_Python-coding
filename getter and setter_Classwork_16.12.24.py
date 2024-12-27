class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self,name):
         self.name=name
    def set_age(self,age):
         self.age=age
name=input("enter the name")
age=int(input("enter the age"))
s=Student(name,age)
n=input()
s.set_name(n)
print(f"The Name is:{s.get_name()}\n Age is:{s.get_age()}")
