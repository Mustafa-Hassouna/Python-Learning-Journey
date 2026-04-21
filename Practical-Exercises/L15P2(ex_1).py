def Isprime(number):
    if number <=1 :
        return False 
    for factor in range(2,number):
        if (number % factor == 0 ):
            return False
    return True
a = int(input("check your number : "))
resulat = Isprime(a)
print("your nmber is ",resulat)