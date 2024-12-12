#HYBRID INHERITANCE
#WITH VARIABLES

class Library:
    def display_library(self):
        print(f"Library Name: {self.name}")

class Book(Library):
    def display_book(self):
        print(f"Book Title: {self.book_title}")

class Member:
    def display_member(self):
        print(f"Member Name: {self.member_name}")

class Transaction(Book, Member):
    def display_transaction(self):
        print(f"Issue Date: {self.issue_date}")
s = Transaction()
s.name = "Sami Library"
s.book_title = "Jurassic Park"
s.member_name = "Preethi"
s.issue_date = "21/9/2020"

s.display_library()
s.display_book()
s.display_member()
s.display_transaction()



