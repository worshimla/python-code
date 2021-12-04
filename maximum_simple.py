a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
if a>b and a>c:
    print(a,"maximum")
elif b>a and b>c:
    print(b,"maximum")
else:
    print(c,"maximum")