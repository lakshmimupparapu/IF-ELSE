a=int(input("enter the unit:"))
if a<100:
    print("No charge")
elif a>=100 and a<200:
    print(a-100,a*5)
elif a>=200:
    print(a-200,a*10)
