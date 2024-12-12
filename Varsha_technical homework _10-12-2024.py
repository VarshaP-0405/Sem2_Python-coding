#PROBLEM--1

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def displayvehicle(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, door, trunk):
        Vehicle.__init__(self,make, model, year)
        self.door = door
        self.trunk = trunk

    def cardisplay(self):
        self.displayvehicle()
        print(f"Number of Doors: {self.door}\nTrunk Capacity: {self.trunk}")

class Truck(Vehicle):
    def __init__(self, make, model, year, axle, cargo):
        super().__init__(make, model, year)
        self.axle = axle
        self.cargo = cargo

    def truckdisplay(self):
        self.displayvehicle()
        print(f"Number of Axles: {self.axle}\nCargo Capacity: {self.cargo}")

class PickupTruck(Car, Truck):
    def __init__(self, make, model, year, door, trunk, axle, cargo,mileage):
        Car.__init__(self, make, model, year, door, trunk)
        Truck.__init__(self, make, model, year, axle, cargo)
        self.mileage=mileage

    def displaypickuptruck(self):
        self.cardisplay()
        self.truckdisplay()
        print("Mileage: ",self.mileage)
        
p = PickupTruck("Chevrolet", "silverado", 2023, 4, "60 cubic feet", 2, "1700 lbs","25mpg")
p.displaypickuptruck()


#PROBLEM--2

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
class Electronics(Product):
    def __init__(self, product_id, name, price, warranty, brand):
        super().__init__(product_id, name, price)
        self.warranty = warranty
        self.brand = brand

    def display_info(self):
        super().display_info()
        print(f"Warranty: {self.warranty} years")
        print(f"Brand: {self.brand}")

class Clothing(Product):
    def __init__(self, product_id, name, price, size, material):
        super().__init__(product_id, name, price)
        self.size = size
        self.material = material

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")
        print(f"Material: {self.material}")
e = Electronics("7007", "Tab", 20000, 4, "Lenova")
c = Clothing("23421", "Lehanga",500, "M", "Cotton")
e.display_info()
c.display_info()

