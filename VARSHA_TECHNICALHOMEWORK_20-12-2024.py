#Question 1
import re
import random
class Member:
     def __init__(self, memid, name, email): 
         self.memid = memid
         self.name = name
         self.email = email
     def verify_email(self):
         ex = r'^[a-z0-9._%+-]+@gmail\.com$'
         if re.match(ex, self.email):
             print("emailid is valid")
         else:
             print("emailid is not valid")
     def verify_member_id(self):
         Id = r'^LIB\d{4}$'
         if re.match(Id, self.memid): 
             print("member id is valid")
         else:
             self.generate_member_id()
     def generate_member_id(self):
         self.member_id = "LIB" + str(random.randint(1000, 9999))
         print(self.member_id)
class Library(Member):
    def __init__(self, memid, name, email, bookid):
        super().__init__(memid, name, email) 
        self.bookid = bookid
    def display_overall(self):
         print("Member id:", self.member_id)
         print("Name:", self.name)
         print("Email:", self.email)
         print("Book borrowed or returned:", self.bookid)
memid = input("Enter the id of the member: ")
name = input("Enter the name: ")
email = input("Enter the email id: ")
bookid = input("Enter the book id: ")
obj= Library(memid, name, email, bookid)
obj.verify_email()
obj.verify_member_id()
obj.display_overall()
