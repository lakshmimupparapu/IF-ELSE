year=int(input("enter the year:"))
month=int(input("enter the month:"))
date=int(input("entre the date:"))
if month<=12:
    if date<=31:
        print(date+1,month,year)
    else:
        print("No")
else:
    print("Invalid data")