import random

class Customer:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade+"th Grade"
        self.student_id = None  
    
    def gen_rand_id(self):
        stu_id = str(random.randint(1000, 9999))
        self.student_id = "STU" + stu_id
    
    def verify_student_id(self):
        if self.student_id and self.student_id[:3] == "STU":
            if len(self.student_id) == 7 and self.student_id[3:7].isdigit():
                print("The ID is verified and is correct")
            else:
                print("The ID is invalid")
        else:
            print("No ID has been generated to verify")
    
    def display_details(self):
        if self.student_id:
            print("The Student ID is", self.student_id)
            print("The Student Name is", self.name)
            print("The Student's Grade is", self.grade)
        else:
            print("No Student ID has been generated")
            print("The Student Name is", self.name)
            print("The Student's Grade is", self.grade)
            
customer = Customer("Varsha", "1")
customer.gen_rand_id()
customer.display_details()
customer.verify_student_id()


