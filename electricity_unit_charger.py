unit=int(input("enter the unit:"))
if unit >= 50:
    bill=unit*0.50
    print(bill,"bill")
elif unit>=100:
    bill=unit*0.75
    print(bill,"bill")
elif unit>100 and unit <250:
    bill=unit*1.20
    print(bill,"bill")
elif unit>250:
    bill=unit*1.50
    print(bill,"bill")
else:
    print("nothing")