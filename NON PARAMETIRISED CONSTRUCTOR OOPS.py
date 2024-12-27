## non parametirised##
class Library:
    def __init__(self):
        self.book_name="Harry Potter"
        self.author_name="J.K.Rowling"
    def display(self):
        print(f"The Book Name is {self.book_name} and the author name is {self.author_name}")
lib=Library()
lib.display()
##parametirised##
class library:
    def __init__(self,book_name,author_name):
        self.book_name=book_name
        self.author_name=author_name
    def display(self):
        print(f"The Book Name is {self.book_name} and the author name is {self.author_name}")
lib=library("Harry Potter")
lib.display()
lib1=library("Sherlock Homes","Sir Arthur Conan Doyle")
lib1.display()
##DEFAULT##
class library:
    def __init__(self,year,book_name="Secret Seven",author_name="Enid Blyton"):
        self.book_name=book_name
        self.author_name=author_name
        self.year=year
    def display(self):
        print(f"The Book Name is {self.book_name} and the author name is {self.author_name} and year of publish is {self.year}")
lib=library(1949)
lib.display()

