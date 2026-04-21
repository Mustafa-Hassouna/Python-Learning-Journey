def fun1(x):
    return x+1
def fun2(x):
    return x**2
def fun3(x):
    return x+2
def k(f,g,h):
    return lambda x:f(g(h(x)))
a = int(input("enter your value please : "))
b = k(fun3,fun2,fun1)
print(b(a))