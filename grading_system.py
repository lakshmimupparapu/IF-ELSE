n=int(input("enter the marks:"))
if n<25:
    print("grade F")
elif n>=25 and n<=45:
    print("grade E")
elif n>45 and n<=50:
    print("grade D")
elif n>50 and n<=60:
    print("grade C")
elif n>60 and n<=80:
    print("grade B")
elif n>80:
    print("grade A")
else:
    print("no grade")