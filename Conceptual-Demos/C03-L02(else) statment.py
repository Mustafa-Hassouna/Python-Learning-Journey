print("Enter Two Values To See What Is The Right Sign Between Theme {  < , > , =  } ")
a = int(input("enter your number : "))
b = int(input("enter your number : "))
if a < b :
    print(a,"<",b)
elif a > b:
    print(a,">",b)
else:
    print(a,"=",b)