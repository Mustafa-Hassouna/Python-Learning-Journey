age = int(input("enter you age to see if you are eligible or not : "))
if age <= 100 and age > 0 :
    if age > 18 :
        print("eligible to vote")
    else:
        print("not eligible to vote")
else:
    print("your age is wrong")