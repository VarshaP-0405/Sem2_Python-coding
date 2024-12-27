class Book:
    def __init__(self):
        self.Book_Name=Book_Name
        self.Author_Name=Author_Name
    def Display(self):
        print("The Name of the Book is",self.Book_Name,"and the Name of the Author is",self.Author_Name)
book1=Book("Sherlock Holmes","Sir Arthur Conan Doyle")
book1.Display()
book1=Book("Secret Seven","Enid Blyton")
book1.Display()
