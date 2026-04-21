def factorial(x):                    # to_much_important
    if (x==0):
        
        return 1
    else:
        x = abs(x)
        return x * factorial(x-1) 
value = int(input("enter your value : "))
result = factorial(value)
print("The Result Or The Factorial Of",value,"Is :",result)