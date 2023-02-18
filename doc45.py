day=int(input("enter the number:"))
if day<=5:
    print(day*2)
elif day>=6 and day<10:
    print(day*3)
elif day>=10 and day<15:
    print(day*4)
elif day>15:
    print(day*5)
else:
    print("No")