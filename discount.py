quantity=int(input("enter the quantity:"))
cost=quantity*100
if cost>1000:
    dis=cost/10
    print(dis,"given discount")
else:
    print("not given discount")