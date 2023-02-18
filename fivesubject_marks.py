a=int(input("enter physics marks:"))
b=int(input("enter chemistry marks:"))
c=int(input("enter biology marks:"))
d=int(input("enter mathematics marks:"))
e=int(input("enter computer marks:"))
total=a+b+c+d+e
per=total/500*100
if per>=90:
    print("grade A")
elif per>=80:
    print("grade B")
elif per>=70:
    print("grade C")
elif per>=60:
    print("grade D")
elif per>=40:
    print("grade E")
elif per<40:
    print("grade F")
else:
    print("No grade")