month=input("enter the month:")
if month in("january","march","may","july","september","december"):
    print("31 days")
elif month in("aprial","june","augest","october","november"):
    print("30 days")
elif month in("february"):
    print("28 days")
else:
    print("No")