a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
if a>b:
    if a>c:
        print("a is maximum")
    elif b>a:
        print("b is maximum")
    else:
        print("c is maximum")
elif b>a:
    if b>c:
        print("b is maximum")
    elif c>b:
        print("c is maximum")
    else:
        print("a is maximum")
elif c>a:
    if c>b:
        print("c is maximum")
    elif a>c:
        print("a is maximum")
    else:
        print("b is maximum")
else:
    print("minimum")