from typing import ByteString


girls=int(input("enter the girls numbers:"))
bed = int(input("enter the bed:"))
if girls > bed or girls==bed:
    a=girls-bed
    if a==0:
        print("equal")
    else:
        print("need",girls-bed,"bed")
else:
    print("need",bed-girls,"girls")

