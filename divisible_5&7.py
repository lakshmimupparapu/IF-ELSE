a=int(input("enter the number:"))
if a>=1500 and a<=2700:
    if a%5==0 and a%7==0:
        print("a is divisible by 7 and 5 and it is between 1500 and 2700")
    else:
        print("a is not divisible by 7 and 5")
else:
    print("it is between 1500 and 2700")