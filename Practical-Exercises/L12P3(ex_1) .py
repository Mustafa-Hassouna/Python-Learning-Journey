# العمليات على رقمان                         
print("menu : \n\t1 : Add\n\t2 : Subtract\n\t3 : Multiply\n\t4 : Divide\n\t5 : Modulus")
choice = int(input("choose your choice : "))
num_1 = float(input("Enter The First Number  : "))
num_2 = float(input("Enter The Second Number : "))
if choice <= 5 and choice >= 1 :
    if choice == 1 :
         result = num_1 + num_2 
    elif choice == 2 :
        result = num_1 - num_2 
    elif choice == 3 :
        result = num_1 * num_2
    elif choice == 4 :
        if num_2 == 0:
            result = "Syntax Error" 
        else:
            result = num_1 / num_2
    elif choice == 5 :
        if num_2 == 0:
            result = "Syntax Error" 
        else:
            result = num_1 % num_2
    print("The Solution of this Is :",result)
else :
    print("erorr in input ! , menu input must be between 1 and 5")
