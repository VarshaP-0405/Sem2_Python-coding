def longest_common_prefix(words):
    if not words:
        return ""

    shortest = min(words, key=len)
    
    for i, char in enumerate(shortest):
        for word in words:
            if word[i] != char:
                return shortest[:i]
    
    return shortest


words = tuple(map(str,input("enter your input").split()))
print("Longest Common Prefix:", longest_common_prefix(words))


###2###
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}, Course: {self.course}")

person_name=input("ENTER PERSON NAME:")
person_age=int(input("ENTER PERSON AGE:"))
student_name=input("ENTER STUDENT NAME:")
student_age=int(input("ENTER STUDENT AGE:"))
student_regno=input("ENTER STUDENT REGISTRATION NUMBER:")
student_dept=input("ENTER STUDENT DEPARTMENT:")
person1 = Person(person_name, person_age)
student1 = Student(student_name, student_age, student_regno, student_dept)
print("\nPerson Details:")
person1.display_info()
print("\nStudent Details:")
student1.display_info()
