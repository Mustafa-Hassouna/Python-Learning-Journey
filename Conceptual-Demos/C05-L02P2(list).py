list = [1,2,3,4,5,6,7,8,9]
print(list[0:6])
for  i in list :
    print(i)
print("--------------------------------------------*--------------------------------------------")
for i in range(len(list)): # range = 0,1,2,3,4,5,6,...          &according
    print(list[i])            # both are the same
print("--------------------------------------------*--------------------------------------------")
print(list[-1])
print(list[4:])
print(list[:5])
print(list[1:9:2])
print(list[1:9:3])
print(list[1:9:4])
print(list[1:9:5])
print(list[1:9:6])
print(list[1:9:7])
print(list[1:9:8])
print(list[1:9:100])
print("--------------------------------------------*--------------------------------------------")
list_1 = [1,2,3]
list_2 = [1,2,3]
print(list_1==list_2)
print(list_1 is list_2)
list_1 = list_2
print(list_1==list_2)
print(list_1 is list_2)
list_2[0] = 2
list_1[0] = 1 
list_3= list_2[:]
print(list_3)
