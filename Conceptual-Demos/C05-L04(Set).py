a_1 = {1,13,4,64,758,9,0,7867,4,5,3,24,}   # Unordered colliction
a_2 = {1,2,3,4,5,6,7,8,9}
print(a_1)
print(a_2)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# generator expreiton with set colliction that's sounds good
a_3 = {i for i in range(10)}
print(a_3)                           # Output : {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
for i in a_3:
    print(i)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
a_4 = {i*3 for i in range(10) if i>5}                # if statment        # excelese       I Don't Know How To  Wirte Wirte 
print(a_4)                                     # Output : {24, 18, 27, 21}
for i in a_4:                                  # Output : 24
                                               #          18                         # Both are the same تمام
                                               #          27      
                                               #          21
    print(i)                                   # I am from german المانية that's sounds good
                                               # we learned today a good things nice to meet you alive agane
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^") # |
list = []                         # 2025/12/29 WOW                     # |
for i in range(10):                                                    # |
    if i>5 :                                                           # |
        list.append(3*i)                                               # |
print(list)                      # output : [18, 21, 24, 27] <-----------|-------------> both are the same  ({24, 18, 27, 21} , [24, 18, 27, 21])