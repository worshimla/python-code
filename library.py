expected_date=int(input("enter the expected_date:"))
expected_month=int(input("enter the expected_months:"))
expected_year=int(input("enter the expected_year:"))
return_date=int(input("enter the return_date:"))
return_months=int(input("enter the return months:"))
return_year=int(input("enter the year:"))
if expected_year==return_year:
    if expected_month==return_months:
        if expected_date==return_date:
             print("fine is",0)
        else:
            print("cost of the book ",15*(return_date-expected_date))
    else:
        print("cost of the book",500*(return_months-expected_date))
else:
    print("cost of the book",1000*(return_year-expected_year))