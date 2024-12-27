#1)Temperature conversion

print("Enter 'c' to convert from clecius to fahrenheit")
print("Enter 'f' to convert from fahrenheit to celcius")
choice=input("Enter your choice:")
if choice=='c':
    celsius=float(input("Enter temperature in celcius"))
    fahrenheit=(celsius*9/5)+32
    print('%.2f Celsius is :%0.2f Fahrenheit'%(celsius,fahrenheit))
elif choice=='f':
    fahrenheit=float(input("Enter temparature in fahreinheit:"))
    celsius=(fahrenheit-32)*5/9
    print('%.2f Fahrenheit is :%0.2f Celsius'%(fahrenheit,celsius))
else:
    print("Invalid Input")
    



