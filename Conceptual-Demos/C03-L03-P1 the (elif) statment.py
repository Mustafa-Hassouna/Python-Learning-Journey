a = int(input("enter the number : "))
b = int(input("enter the number : "))
c = int(input("enter the number : "))
# a>b and a>c 
# b>a and b>c
# c>a and c>b
# a=b>c
# b=c>a
# c=a>b
if a>b and a>c:
    print(a,"Is the greater")
elif b>a and b>c:
    print(b,"Is the greater")
elif c>a and c>b:
    print(c,"Is the greater")
elif a==c==b :
    print("All the inputs are equal")
elif a==b>c:
    print("the first input snd the second are equal and the beggier")
elif b==c>a:
    print("the second input snd the last are equal and the beggier")
elif c==a>b:
    print("the first input snd the last are equal and the beggier")
else:
    print("There is something wrong")