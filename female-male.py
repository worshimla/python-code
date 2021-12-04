employee=input("enter the sex:")
age=int(input("enter the age:"))
if employee=="female":
    print("work place in urban area")
elif employee=="male":
    if age>=20<=40:
        print("he may work in anywere")
elif employee=="male":
    if age>40<60:
         print("work in urban")
else:
    print("error")