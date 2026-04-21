print("<------------------------- Enter The Values You Need To Add ------------------------->")
b = 0
while (True) :
    a = float(input("enter the value : "))
    b = a + b
    if a == 0 :
        print(b)
        print("----------------------------------------------------------------------------------")
        break