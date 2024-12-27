class Inventory:
    def getInventoryInfo(self):
        self.Pid=input("Enter the Product ID:")
        self.Pname=input("Enter the Product Name:")
        self.Pcount=int(input("Enter the Product Count:"))
    def displayInventoryInfo(self):
        print("ID = ",self.Pid,"\nName = ",self.Pname,"\nCount = ",self.Pcount)


p=Inventory()
p.displayInventoryInfo()
