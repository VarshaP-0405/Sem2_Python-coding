class Employee:
    def _init_(self,eid,ename,eposition):
        self.eid=eid
        self.ename=ename
        self.eposition=eposition
    def display(self):
        print("The employee ID is:",self.eid,"\n The employee Name is:",self.ename,"\n The employee Position is:",self.eposition)
class Address:
    def _init_(self,Country,State,Street):
        self.Country=Country
        self.State=State
        self.Street=Street
    def display_address(self):
        print("The country the employee lives is:",self.Country,"\nThe State the employee lives is:",self.State,"\nThe Street the employee lives is:",self.Street)
class EmployeeDetails(Employee,Address):
    def _init_(self,eid,ename,eposition,Country,State,Street):
        super()._init_(eid,ename,eposition)
        Address._init_(self,Country,State,Street)
    def displayEmp(self):
        self.display()
        self.display_address()
ID=int(input("enter id"))
Name=input("enter name")
position=input("enter the position")
country=input("enter the country")
state=input("enter the state")
street=input("enter the street")
emp_det=EmployeeDetails(ID,Name,position,country,state,street)
emp_det.displayEmp()
