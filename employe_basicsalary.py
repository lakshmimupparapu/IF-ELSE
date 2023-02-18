basicsalary=int(input("enter the basic salary:"))
if basicsalary<=10000:
    HRA=20/100*basicsalary
    DA=80/100*basicsalary
    print(HRA+DA+basicsalary)
elif basicsalary<=20000:
    HRA=25/100*basicsalary
    DA=90/100*basicsalary
    print(HRA+DA+basicsalary)
elif basicsalary>20000:
    HRA=30/100*basicsalary
    DA=95/100*basicsalary
    print(HRA+DA+basicsalary)
else:
    print("enter valid data")

