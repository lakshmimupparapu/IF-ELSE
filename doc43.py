age=int(input("enter the age:"))
gender=input("enter the gender:")
days=int(input("enter the days:"))
if age>=18 and age<30:
    gender=="m"
    wages=700*days
    print("total amount",wages)
elif age>=18 and age<30:
    gender=="f"
    wages=750*days
    print("total amount",wages)
elif age>=30 and age<=40:
    gender=="m"
    wages=800*days
    print("total amount",wages)
elif age>=30 and age<=40:
    gender=="f"
    wages=850*days
    print("tatol amount",wages)
else:
    print("No")