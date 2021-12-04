language=input("choose the language:")
if language=="english":
    print("welcome to State Bank of India")
    secret_pin=input("enter the secret pin:")
    if secret_pin=="1224":
        select=input("withdraw or deposit or balance inquiry:")
        balance="50000"
        if select=="withdraw":
            amount=int(input("enter the amount:"))
            if amount<=10000:
                print("processing")
                print(50000-amount,"is the left balance")
            else:
                print("above 10000 cannot be withdraw")
        if select=="balance enquiry":
            print("your total balance",50000)
        if select=="deposit":
            deposit=int(input("enter the deposit amount:"))
            print(deposit+50000,"your current balance")
        if select=="exit":
            print(" thank you for visiting")
else:
    print("error pin")
