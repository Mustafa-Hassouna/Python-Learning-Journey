# # 1  ===> 30*1  +1 
# # 2  ===> 30*2  +1 (-1 or -2) 
# # 3  ===> 30*3  +2 (-1 or -2) 
# # 4  ===> 30*4  +2 (-1 or -2) 
# # 5  ===> 30*5  +3 (-1 or -2) 
# # 6  ===> 30*6  +3 (-1 or -2) 
# # 7  ===> 30*7  +4 (-1 or -2) 
# # 8  ===> 30*8  +4 (-1 or -2) 
# # 9  ===> 30*9  +5 (-1 or -2) 
# # 10 ===> 30*10 +5 (-1 or -2) 
# # 11 ===> 30*11 +6 (-1 or -2) 
# # 12 ===> 30*12 +6 (-1 or -2) 

# month = int(input("enter the month : "))
# year = int(input("enter the year : "))
# days = month * 30
# if month==1:
#     print("number of days is : " , days + 1)
# elif (month >= 2 and month <= 12):
#     extra = (month + 1)//2
#     if (year % 400 == 0 or (year % 4==0 and year % 100 != 0)):
#         days = days - 1
#     else:
#         days = days - 2
#     print("number of days is : " , days + extra)
# else:
#     print("erorr in input")

month = int(input("enter the month : "))
year = int(input("enter the year : ")) 
days = month*30 
if month == 1 :
    print("number of days is : " , days + 1)
elif (month <= 12) and (month >= 2) and (year > 0):
    if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        days == days - 1
    else:
        days == days - 2
    extra = (month + 1) // 2
    print("number of days is : " , days + extra)
else:
    print("error in input")