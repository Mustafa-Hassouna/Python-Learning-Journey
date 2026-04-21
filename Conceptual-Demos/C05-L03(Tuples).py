a_1 = 1,2,3              # output:(1,2,3)       # To Id A Tuple 
a_2 = (1,2,3)            # output:(1,2,3)
a_3 = [1,2,3]                                   # All Of theme (a_1,a_2,a_3,a_4,a_5) Are The Same . 
a_4 = tuple(a_3)         # output:(1,2,3)              
a_5 = tuple([1,2,3])     # output:(1,2,3)             
print(a_1)               #                            Mustafa Hassouna 2025/12/29
print(a_2)
print(a_4)
print(a_5)
print("---------------------------------^---------------------------------")
for i in a_1 :                       # a_1 : Is A Tuple (1,2,3)
    print(i)
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
for i in range(len(a_1)):
    print(a_1[i])
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
a_6 = (1,1,1,2,2,2,3,3,3)      # a_6 : is a new tuple
a_7 = a_6.count(3)             # just to explan a count function or module
print(a_7)
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
a_8 = a_6.index(3)             # the index of (3)
print(a_8)
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
a_9 = len(a_6)                 # a_6 : Is the tuple of (1,1,1,2,2,2,3,3,3) Mustafa Hassouna 2025/12/29
print(a_9)
print("<><><><><><><><><><><><><><><><><><><><><><><><><><><>")
# Sliceing
b_1 = (1,2,3,4,5,6,7,8,9)
     # 0,1,2,3,4,5,6,7,8
b_2 = b_1[0:6]
b_3 = b_1[0:]
b_4 = b_1[:5]
b_5 = b_1[0:9:2]
print(b_2)        # Output : (1, 2, 3, 4, 5, 6)           from b_1 = (1,2,3,4,5,6,7,8,9) Tuple
print(b_3)        # Output : (1, 2, 3, 4, 5, 6, 7, 8, 9)  from b_1 = (1,2,3,4,5,6,7,8,9) Tuple
print(b_4)        # Output : (1, 2, 3, 4, 5)              from b_1 = (1,2,3,4,5,6,7,8,9) Tuple
print(b_5)        # Output : (1, 3, 5, 7, 9)              from b_1 = (1,2,3,4,5,6,7,8,9) Tuple
print("<<<<<<<<>>>>>>>><<<<<<<<>>>>>>>><<<<<<<<>>>>>>>><<<<<<<<>>>>>>>>")
# Tupls & Functions                   let's see ("look or whatever")
def f():

    return 1,2,3
print(f())      # output : (1, 2, 3)           simple and easy hahaha    Mustafa Hassouna 2025/12/29
print("<<<<<<<<>>>>>>>><<<<<<<<>>>>>>>><<<<<<<<>>>>>>>><<<<<<<<>>>>>>>>")
# exaple about Tupls & Functions
def cirAndArea(x):
    cir = 2 * 3.14 * x
    area = 3.14 * x * x
    return cir , area
print(cirAndArea(11))      # output : (69.08, 379.94)
print("<<<<<<<<>>>>>>>><<<<<<<<>>>>>>>><<<<<<<<>>>>>>>><<<<<<<<>>>>>>>>")
# Generator Expresion     <genexpr>
b_6 = 1,2,3,4,5
b_7 = (i for i in b_6)
print(b_7)                 # output : <generator object <genexpr> at 0x0000020414A65E40>
for i in b_7:
    print(i)               # output : 1
                           #          2    
                           #          3    
                           #          4    
                           #          5    
print("<<<<<<<<>>>>>>>><<<<<<<<>>>>>>>><<<<<<<<>>>>>>>><<<<<<<<>>>>>>>>")
b_7 = (i*2 for i in b_6)
print(b_7)                 # output : <generator object <genexpr> at 0x0000020414A65E40>
for i in b_7:
    print(i)               # output : 2
                           #          4    
                           #          6    
                           #          8    
                           #          10    
print("<<<<<<<<>>>>>>>><<<<<<<<>>>>>>>><<<<<<<<>>>>>>>><<<<<<<<>>>>>>>>")
b_8 = (i for i in [1,2,3])
for i in b_8:
    print(i)
print("<<<<<<<<>>>>>>>><<<<<<<<>>>>>>>><<<<<<<<>>>>>>>><<<<<<<<>>>>>>>>")

#                              الى هنا نكون قد انتهينى    