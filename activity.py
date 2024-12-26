num = int(input("enter number to cheack if you are eligible voter:"))
if num>17:
    print("age greater than 17")
    if num%2==0:
        print("you are eligible")
    else:
        print("you are not eligible ")
else:
    ("age is less than 50")