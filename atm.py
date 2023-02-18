from gettext import translation


print("welcome to SBI bank")
print("insert your card")
print("select your language")
language=input("enter the language:")
if language=="english":
    amount=60000
    pin=int(input("enter the pin:"))
    if pin==5656:
        print("transtion:1.withdraw,2.balance enquery,3.pin generation,4.deposit,5.exit")
        transtion=int(input("enter the transtion:"))
if transtion==1:
    withdraw=int(input("enter the withdraw amount:"))
    if withdraw<=amount:
        print("collect your withdraw cash")
        print("reaming balance is",amount-withdraw)
    else:
        print("no withdraw")
elif transtion==2:
    print("avalible balance is",amount)
    print("than you")
elif transtion==3:
    pin_generation=int(input("enter the new pin:"))
    if pin==5656:
        print("your new pingeneration is successfully completed")
    else:
        print("try again")
elif transtion==4:
    deposit=int(input("enter the deposit amount:"))
    if deposit>=2000:
        print("completed your deposit amount",amount+deposit)
    else:
        print("not deposit")
elif transtion==5:
    print("exit")
    print("thank you")
else:
    print("enter valid data")