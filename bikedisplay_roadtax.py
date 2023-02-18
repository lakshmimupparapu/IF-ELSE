amt=int(input("enter the amount:"))
if amt>100000:
    tax=amt*15/100
    print(tax)
elif amt<=50000 and amt<=100000:
    tax=amt*10/100
    print(tax)
elif amt<=50000:
    tax=amt*5/100
    print(tax)
else:
    print("No tax")