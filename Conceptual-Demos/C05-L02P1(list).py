list = [1,2,3,4,5,6,7,8,9,10] # اصبر و ما صبرك الا بالله
a = list.append(11)
a_1 = list.append([12,13])
a_2 = list.pop(-1)
a_3 = list.clear()
a_4 = list.extend([3,2,1])
a_5 = list.extend([0])        # [3, 2, 1, 0]
a_6 = list.append(-1)
a_7 = list.pop(-1)
a_8 = list.extend([-1])       # [3, 2, 1, 0, -1]
a_9 = list.insert(0,1)
b_1 = list.extend([1,1,1,1,1])   # [1, 3, 2, 1, 0, -1, 1, 1, 1, 1, 1]
b_2 = list.count(1)
b_3 = list.clear()            # []
b_4 = list.extend([1,2,3,4,5,6,7,8,9])
b_5 = list.pop(8)
b_6 = list.insert(8,9)        # [1, 2, 3, 4, 5, 6, 7, 8, 9] hahaha
b_5 = list.pop(0)
b_6 = list.insert(0,1)        # [1, 2, 3, 4, 5, 6, 7, 8, 9]
b_7 = list.remove(1)
b_8 = list.insert(0,1)        # [1, 2, 3, 4, 5, 6, 7, 8, 9]
b_9 = list.reverse()
c_1 = list.sort()
c_2 = list.reverse()
c_3 = list.sort()             # [1, 2, 3, 4, 5, 6, 7, 8, 9]
c_4 = len(list)
del(list[0])
c_5 = list.insert(0,1)        # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list)                     # Me Is The Winner Isn't Me               Suck My Nothing I'm Sorry To Say That Babe . . . // We Live To Die Don't We Please God Help Us We_Are_From_Gaza$ 
print("-------------------------------واو-------------------------------")  
c_6 = [1,2,3]
c_7 = [4,5,6]
c_8 = [7,8,9]
c_9 = c_6 + c_7 + c_8         # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(c_9)
d_1 = c_6 * 3
print(d_1) 
for i in c_9:
    print(i)
print("-------------------------------واو-------------------------------")  
d_2 = [1,2,3,4,5,6,7,8,9]
print(10 in d_2)