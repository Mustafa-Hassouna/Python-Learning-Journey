def power(a,b):
    result = 1
    for i in range(b):
        result *= a
    return result  
num_1 = int(input("enter the base : "))
num_2 = int(input("enter the exp : "))
result = power(num_1,num_2)
print("the power of the number is " , result)