age1=int(input("enter the age1:"))
age2=int(input("enter the age2:"))
age3=int(input("enter the age3:"))
if age1> age2 and age1>age3:
    print(age1,"oldest")
elif age2>age1 and age2>age3:
    print(age2,"youngest")
elif age3>age1 and age3>age2:
    print(age3,"younger")
else:
    print("all are equal")