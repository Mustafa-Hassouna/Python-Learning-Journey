print("====> enter your three grads to calc the total by percentage and this sighns (A,B,C,D,F) <====")
mark_1 = float(input("enter the first score : "))
mark_2 = float(input("enter the second score : "))
mark_3 = float(input("enter the third score : "))
percentage = (mark_1 + mark_2 + mark_3)/3
mark_if_1 = mark_1 < 100 and mark_1 > 0
mark_if_2 = mark_2 < 100 and mark_2 > 0
mark_if_3 = mark_3 < 100 and mark_3 > 0
if (mark_if_1) and (mark_if_2) and (mark_if_3):
    if percentage >= 90 :
        print("your grade is A and your grade by percentage is : %5.2f" %(percentage),"%")
    elif percentage >= 80 :
        print("your grade is B and your grade by percentage is : %5.2f" %(percentage),"%")
    elif percentage >= 70 :
        print("your grade is C and your grade by percentage is : %5.2f" %(percentage),"%")
    elif percentage >= 50 :
        print("your grade is D and your grade by percentage is : %5.2f" %(percentage),"%")
    elif percentage < 50 :
        print("your grade is F and your grade by percentage is : %5.2f" %(percentage),"%")
else:
    print("your ave is wrong " \
    "it must be between 0-100 ")
print("I Am Here To Make The Life Easier")   

print()