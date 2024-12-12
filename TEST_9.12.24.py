name=input()
roll_no=int(input())
class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def show(self):
        print("Name=",self.name)
        print("Roll Number=
