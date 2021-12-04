price=int(input("enter the price:"))
if price >100000:
    print("tax",15/100*price)
elif price>50000 and price<=100000:
    print("tax",10/100*price)
elif price<=50000:
    print("tax",5/100*price)
else:
    print("no tax")