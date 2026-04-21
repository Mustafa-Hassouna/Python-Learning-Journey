################version(1)##################
# average_1 = input("Enter Your Average : ")
# average = float(average_1)
# if average <= 100 and average >= 90 :
#     print("Your Average Is Excellent") 
# elif average < 90 and average >= 80 :
#     print("Your Average Is Very Good")
# elif average < 80 and average >= 70 :
#     print("Your Average Is Good")
# elif average < 70 and average >= 50 :
#     print("Your Average Is pass")
# elif average < 50 and average >= 0 :
#     print("Your Average Is fial")
# else:
#     print("errer")
################version(2)##################                      #Mustafa Hassouna * 2025/11/20 *
average = float(input("Enter Your Average : "))

if average<100 and average>0:
    if average >= 90 :
        print("Your Average Is Excellent") 
    elif average >= 80 :
        print("Your Average Is Very Good")
    elif average >= 70 :
        print("Your Average Is Good")
    elif average >= 50 :
        print("Your Average Is pass")
    else:
        print("Your Average Is fial")
else:
    print("errer")

