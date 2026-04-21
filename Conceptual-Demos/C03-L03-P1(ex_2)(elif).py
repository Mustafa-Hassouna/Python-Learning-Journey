a = int(input("enter your value : "))      # 2025/12/31
b = int(input("enter your value : ")) 
c = int(input("enter your value : ")) 

if a > b and a > c:
    print(a,"is the greeter.")
elif b > a and b > c:
    print(b,"is the greeter.")
elif c > b and c > a:
    print(c,"is the greeter.")
elif c == b == a:
    print("All are equal")
elif a==b and b > c and a>c:
    print(a,"and",b,"are the greeter.")


    