print("ELIGIBLE FOR SALARY")
a=int(input("enter your age :"))
b=int(input("enter your salry:"))
if a>=21 and a<=60:
    if  b>=25000:
        print("eligible")
    else:
        print("not eligible")
else:
    print("not eligble for age")
