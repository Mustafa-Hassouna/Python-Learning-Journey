# العمليات على رقمان                         
while (True) :
    print("menu : \n\t" \
    "1 : Add\n\t" \
    "2 : Subtract\n\t" \
    "3 : Multiply\n\t" \
    "4 : Divide\n\t" \
    "5 : Modulus\n\t" \
    "6 : To End The Programe")
    choice = int(input("choose your choice : "))
    if choice == 6 :
        for i in range(6):
            print("<-------------------------------------- The Programme Ended -------------------------------------->")
        break
    if (choice <= 1 or choice >= 6):
        print("error in input ! , menu input must be between 1 and 6")
        print("-----------------------------------------------------------------------------------------------------")
        continue
    num_1 = float(input("Enter The First Number  : "))
    num_2 = float(input("Enter The Second Number : "))
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
    print("-----------------------------------------------------------------------------------------------------")