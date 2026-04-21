print("========================= Quizzes =========================")
q1 = int(input("enter the score of the first quiz : "))
q2 = int(input("enter the score of the second quiz : "))
q3 = int(input("enter the score of the third quiz : "))
print("========================= mid-term =========================")
mid = int(input("enter the score of the mid-term : "))
print("========================= final =========================")
final = int(input("enter the score of the final : "))
print("========================= results =========================")
Quiz_Total = q1+q2+q3
print("Quiz Total : ",Quiz_Total)
print("mid-term : ",mid)
print("final : ",final)
print("========================= Total =========================")
final_total = Quiz_Total + final + mid 
percentage = final_total/5 
print(final_total,"from 500", "and the percentage",percentage,"%")
