class Employee:
    def getEmployeeInfo(self):
        self.id=input('Enter  ID:')
        self.name=input('Enter Your Name:')
        self.salary=int(input('Enter Your Salary'))
    def displayEmployeeInfo(self):
        print("ID={self.id}\n Name={self.name}\n Salary={self.salary}")
    def getSalary(self):
        return self.salary
class Perks(Employee):
    def calculateSalary(self):
        self.getEmployeeInfo()
        sal=self.getSalary()
        self.hra=sal*15/100
        self.da=sal*14/100
        self.total=self.hra+self.da
##2##
class Employee:
    def getEmployeeInfo(self):
        self.id=input('Enter  ID:')
        self.name=input('Enter Your Name:')
    def displayEmployeeInfo(self):
        print("ID=",self.id,"\nName=",self.name)
class Perks(Employee):
    def getDetails(self):
        self.getEmployeeInfo()
        self.sal=int(input("Enter the salary"))
    def displayInfo(self):
           self.displayEmployeeInfo()
           print("salary=",self.sal)
p=Perks()
p.getDetails()
p.displayInfo()










        
        
