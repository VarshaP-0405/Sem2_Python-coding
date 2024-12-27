try:
    def Calculate_fare(mile,minu,Surge,base=2.50):
        fare=base+(1.50*mile)+(0.25*minu)
        if Surge>0:
            tot_fare=fare*Surge
            return tot_fare
        else:
            return fare
    mile=float(input("enter the miles"))
    minute=float(input("enter the minutes"))
    Surge=float(input("enter the Surge"))
    if mile<0 or minute<0:
        raise ValueError("Enter only positive values for mile and minute")
    else:
        total_fare=Calculate_fare(mile,minute,Surge)
        print("The Total Fare is:",total_fare)
except ValueError:
    print("Enter only positive values for mile and minute")
