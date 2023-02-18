amount=(int(input("enter the amount:")))
if amount>1000:
    discount=amount*0.1
    total=amount-discount
    print(total)
else:
    print("no discount")
    