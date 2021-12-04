classesheld=int(input("enter the no of class held:-"))
classesattendents=int(input("enter the no of class attendent:-"))
percentage=classesattendents/classesheld*100
print(percentage)
# if percentage<75:
#     print("yes")
# else:
#     print("not")

if percentage>=75:
    print("allowed to sit in exam")
else:
    print("not allowed to sit in exam")