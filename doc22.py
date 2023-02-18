year=int(input("enter the year:")) 
salary=int(input("enter the salary:"))
if year>5:
    a=year-5
    b=a*100
    print(salary+b)
else:
    print("no bouns")