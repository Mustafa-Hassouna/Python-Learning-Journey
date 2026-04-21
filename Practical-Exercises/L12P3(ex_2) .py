print("<========== Enter three values to see what is the  biggest value ==========>")
num_1 = float(input("Enter the first  number : "))
num_2 = float(input("Enter the second number : "))
num_3 = float(input("Enter the third  number : "))
max = num_1
if num_2 > num_1 :
    max = num_2
if num_3 > num_1 :
    max = num_3
print("the biggest value is :",max)

