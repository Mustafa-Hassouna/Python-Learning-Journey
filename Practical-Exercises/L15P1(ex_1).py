# def factorial(num):
#     x = 1
#     for i in range(1,num+1):
#         x *= i
#     return x
# number = int(input("enter an integer and positive number : "))
# result = factorial(number)
# print("The Factorial Of ",number,"Is",result)
# -----------------------------------------------------------------------------
# def factorial(num):
#     x=1
#     for i in range(1,num+1):
#         x *= i
#     return x
# number = int(input("enter an integer and positive number : "))
# result = factorial(number)
# print("The Factorial Of ",number,"Is",result)
def factorial(num):
    x = 1
    for i in range(1,num+1):
        x *= i
    return x 
number = int(input("enter an integer position number : "))
result = factorial(number)
print("factorial of the number is " , result)