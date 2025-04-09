class Employee:
    def __init__(self, name, emp_id, salary):
        """Initialize employee details."""
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        """Display employee details."""
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Monthly Salary: ${self.salary:.2f}")

    def calculate_yearly_salary(self):
        """Calculate and return yearly salary."""
        return self.salary * 12
name=input("Enter Name:")
empid=int(input("Enter Employee ID:"))
salary=int(input("Enter Monthly Salary"))
emp1 = Employee(name,empid,salary)
emp1.display_info()
print(f"Yearly Salary: ${emp1.calculate_yearly_salary():.2f}")
##2##
class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def display_info(self):
        
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, department, salary):
        super().__init__(name, emp_id, department)
        self.salary = salary
    def calculate_annual_salary(self):
       return self.salary * 12
    def display_full_time_info(self):
        self.display_info()
        print(f"Monthly Salary: ${self.salary:.2f}")
        print(f"Annual Salary: ${self.calculate_annual_salary():.2f}\n")


class PartTimeEmployee(Employee):
   
    
    def __init__(self, name, emp_id, department, hourly_rate, hours_worked):
        super().__init__(name, emp_id, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        """Calculate total salary based on hours worked."""
        return self.hourly_rate * self.hours_worked

    def display_part_time_info(self):
        """Display part-time employee details."""
        self.display_info()
        print(f"Hourly Rate: ${self.hourly_rate:.2f}")
        print(f"Hours Worked: {self.hours_worked}")
        print(f"Total Earnings: ${self.calculate_salary():.2f}\n")


#Full-Time 
name=input("Enter Name:")
dept=input("Enter Department:")
empid=int(input("Enter Employee ID:"))
salary=int(input("Enter Monthly Salary"))
full_time_emp = FullTimeEmployee(name, empid, dept,salary)
full_time_emp.display_full_time_info()
#Part-Time 
pa_name=input("Enter Name:")
pa_dept=input("Enter Department:")
pa_empid=int(input("Enter Employee ID:"))
pa_hourlyrate=int(input("Enter hourly rate"))
pa_hoursworked=int(input("enter hours worked"))

part_time_emp = PartTimeEmployee(pa_name,pa_empid,pa_dept,pa_hourlyrate,pa_hoursworked)
part_time_emp.display_part_time_info()

