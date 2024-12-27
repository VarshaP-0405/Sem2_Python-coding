try:
    class StudentMarks:
        def __init__(self,name,marks):
            self.name=name
            self.marks=marks
        def calculate_grade(self):
            if self.marks>=90 and self.marks<=100:
                print("Grade A")
            elif self.marks>=80 and self.marks<=89:
                print("Grade B")
            elif self.marks>=70 and self.marks<=79:
                print("Grade C")
            elif self.marks>=60 and self.marks<=69:
                print("Grade D")
            else:
                print("Grade F")
    Name=input("Enter your Name")
    mark=int(input("enter your mark"))
    if len(Name)<0 or Name!=str(Name) or mark>100 or mark<0 or mark!=float(mark):
        raise ValueError()
    else:
        print("The Student Name is",Name)
        print("The Student Grade is")
        check=StudentMarks(Name,mark)
        check.calculate_grade()
except ValueError :
    print("ERROR ,NAME IS EMPTY OR NOT A STRING OR MARKS IS OUT OF RANGE OR NOT A NUMBER")
    










    
