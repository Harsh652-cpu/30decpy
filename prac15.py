Activities_weightage=30.0
sports_weightage=20.0
exams_weightage=50.0
exams_total=200.0
ACTIVITIES_TOTAL=60.0
sports_total=50.0
exam_score1=int(input("Enter the marks in first examination(out of 100):"))
exams_score2=int(input("Enter the marks in second examination(out of 100:"))
sports_score=int(input("Enter the score obtained in sports activities(out of 50):-"))
activities_score1=int(input("Enter the marks in first activity(out of 20):-"))
activities_score2=int(input("Enter the marks in second activity(out of 20):-"))
activities_score3=int(input("Enter the marks in third activity(out of 20):-"))
exam_total=exam_score1+exams_score2
activities_total=activities_score1+activities_score2+activities_score3
exam_percent=float(exam_total*exams_weightage/exams_total)
sports_percent=float(sports_score*sports_weightage/sports_total)
activities_percent=float(activities_total*Activities_weightage/ACTIVITIES_TOTAL)
total_percent=exam_percent+sports_percent+activities_percent
print("\n \n \n **********RESULT***********")
print("\n Total percent in examination:-"+str(exam_percent))
print("\nTotal percent in activities:-"+str(activities_percent))
print("\nTotal percent in sports:-"+str(sports_percent))
print("\n ----------------------")
print("\nTotal Percent:-"+str(total_percent))

