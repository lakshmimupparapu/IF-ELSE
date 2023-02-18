year=int(input("enter the year:"))
month=int(input("enter the month:"))
date=int(input("enter the date:"))
hour=int(input("enter the hour:"))
min=int(input("enter the minute:"))
sec=int(input("enter the seconds:"))
if month>=1 and month<=12:
    if date>=1 and date<=31:
        if hour>=1 and hour<=24:
            if min>=1 and min<=60:
                if sec>=1 and sec<=60:
                    print(year,"-",month,"-",date,"-",hour,"-",min,"-",sec)
                else:
                    print("Missing seconds")
            else:
                print("Missing minutes")
        else:
            print("Missing hour")
    else:
        print("Missing date")
else:
    print("Enter the valid data")
    