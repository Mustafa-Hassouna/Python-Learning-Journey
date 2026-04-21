def Isprime(number):
    if number <=1 :
        return False 
    sum = 0
    for factor in range(1,number):
        if (number % factor == 0 ):
            sum = sum + factor
    return sum 
    if sum == number :    
        print(True)
    else :
        print(False)
a = int(input("check your number : "))
resulat = Isprime(a)
print("your nmber is ",resulat)