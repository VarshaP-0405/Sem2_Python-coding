try:
    class ecomm:
        def totprice(self, price, disc, tax):
            
            disc= price * (disc / 100)
            tax = price * (tax/ 100)
            total = price - disc+ tax
            print(f"Price: {total:.2f}")
    obj= ecomm() 

    price = float(input("Enter price: "))
    discount = float(input("Enter discount percentage: "))
    tax= float(input("Enter tax percentage: "))
    if price <= 0 or discount<= 0 or tax <= 0:
                raise ValueError()
    else:
        obj.totprice(price, discount, tax)
except ValueError:
    print("Value Error,value must be positive")
