class Library:
    def _init_(self,bookid,bookname,bookgenere):
        self.bookid=bookid
        self.bookname=bookname
        self.bookgenere=bookgenere
    def display(self):
        print("The Book ID is:",self.bookid,"\n The Book Name is:",self.bookname,"\n The Book Genere is:",self.bookgenere)
class Member:
    def _init_(self,MembershipId,MemberName,MemberAge):
        self.MembershipId=MembershipId
        self.MemberName=MemberName
        self.MemberAge=MemberAge
    def display_member(self):
        print("The MembershipId of the person is:",self.MembershipId,"\nThe Name of the member is:",self.MemberName,"\nThe Age of the member is:",self.MemberAge)
class LibraryManagement(Library,Member):
    def _init_(self,bookid,bookname,bookgenere,MembershipId,MemberName,MemberAge):
        super()._init_(bookid,bookname,bookgenere)
        Address._init_(self,MembershipId,MemberName,MemberAge)
    def displayLib(self):
        self.display()
        self.display_member()
bookid=int(input("enter bookid"))
bookname=input("enter bookname")
bookgenere=input("enter the bookgenere")
MembershipId=int(input("enter the MembershipId"))
MemberName=input("enter the MemberName")
MemberAge=int(input("enter the MemberAge"))
Lib_det=LibraryManagement(bookid,bookname,bookgenere,MembershipId,MemberName,MemberAge)
Lib_det.displayLib()
#Question 2
class Restaurant:
    def _init_(self,foodname,food ingredients,food recipie):
        self.foodname=foodname
        self.food ingredients=food ingredients
        self.food recipie=food recipie
    def display(self):
        print("The Food Name is:",self.foodname,"\n The Food Ingredients are:",self.self.food ingredients,"\n The Food Recipie is:",self.food recipie)
class Delivery:
    def _init_(self,DeliveryId,FoodDeliveryPersonName,FoodDeliveryPersonPhonenumber):
        self.DeliveryId=DeliveryId
        self.FoodDeliveryPersonName=FoodDeliveryPersonName
        self.FoodDeliveryPersonPhonenumber=FoodDeliveryPersonPhonenumber
    def display_member(self):
        print("The DeliveryId  is:",self.MembershipId,"\nThe Name of the Food Delivery Person is:",FoodDeliveryPersonName,"\nThe Food Delivery Person's Phone Number is:",self.FoodDeliveryPersonPhonenumber)
class Order(Library,Member):
    def _init_(self,foodname,food ingredients,food recipie,DeliveryId,FoodDeliveryPersonName,FoodDeliveryPersonPhonenumber):
        super()._init_(foodname,food ingredients,food recipie)
        Address._init_(self,DeliveryId,FoodDeliveryPersonName,FoodDeliveryPersonPhonenumber)
    def displayRes(self):
        self.display()
        self.display_member()
foodname=input("enter foodname")
food ingredients=input("enter food ingredients")
food recipie=input("enter the food recipie")
DeliveryId=int(input("enter the DeliveryId"))
FoodDeliveryPersonName=input("enter the FoodDeliveryPersonName")
FoodDeliveryPersonPhonenumber=int(input("enter the Food Delivery Person Phonenumber"))
Res_det=Order(foodname,food ingredients,food recipie,DeliveryId,FoodDeliveryPersonName,FoodDeliveryPersonPhonenumber)
Res_det.displayRes()
