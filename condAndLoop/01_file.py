#   Conditional Statements Example
score=85

if score > 100:
    print("invalid score out of 100")
    exit()    #  exit() or break used to return from the further loop  

if score > 90 :
    print("A grade")
elif score > 80 :
    grade = "B"
    print("B grade")
elif score > 70 :
    print("C grade")
else :
    print("D grade")

#   Loop Example
for i in range(5) :
    print("Iteration number :", i)  


age=26
day="sunday"

price=12 if age >= 18 else 6  # one liner statement

if(day=="sunday"):  # () is optional 
    price +=2


dist=3

if dist > 10:
    activity="donot walk"
elif dist < 3:
    activity="walk"

print(activity)

year=2025

# () is required when we are checking two or more conditions otherwise it is optional
if(year % 4==0 and year % 100 !=0) or (year % 400 ==0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")


    





