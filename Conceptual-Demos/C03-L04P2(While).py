print("the Even numbers from 1 to 10") 
i = 2
while i <= 10 :
    print(i,end="\t")
    i = i + 2
print("\n")
# <<<<<<<<<<<<<<>>>>>>>>>>>>>>>
print("the Odd numbers from 1 to 10") 
i = 1
while i <= 10 :
    print(i,end="\t ")
    i = i + 2
print("\n")
# <<<<<<<<<<<<<<>>>>>>>>>>>>>>>
print("the numbers can division to 3 from [1 to 20] ") 
i = 3
while i <= 20 :
    print(i,end="\t ")
    i = i + 3
print("\n")
# <<<<<<<<<<<<<<>>>>>>>>>>>>>>>
print("to fine the summation from [1,5]") 
a = int(input("enter your value : "))
b = 0
c = 0
while c <= 3 :   # 1+2+3+4 = 10  
    b = b + a    # 2+3+4+5 = 14   
    a = a + 1         
    c = c + 1         
print(b)
