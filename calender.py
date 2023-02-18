date=int(input("enter the date:"))
month=int(input("enter the month:"))
year=int(input("enter the year:"))
if month==4 or month==6 or month==9 or month==11:
    if date<30:
        print(date+1,"-",month,"-",year)
    else:
        print("1","-",month+1,"-",year)
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
    if date<31:
        print(date+1,"-",month,"-",year)
    else:
        print("1","-",month+1,"-",year)
elif month==12:
    if date<31:
        print(date+1,"-",month,"-",year)
    else:
        print("1","-","1","-",year+1)
elif year%4!=0:
    if month==2:
        if date<28:
            print(date+1,"-",month,"-",year)
        else:
            print("1","-",month+1,"-",year)
    else:
        print("nonthing")
elif year%4==0:
    if month==2:
        if date<29:
            print(date+1,"-",month,"-",year)
        else:
            print("1","-",month+1,"-",year)
    else:
        print("Nonthing")
else:
    print("Invalid data")