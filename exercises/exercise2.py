"""
exercise: grade calculator
write a program that prompts the user to enter in their grades on assignments one at a time until they enter "compute"
assume the user will give you a valid input
compute and print a float of their grade average
after their average, print their letter grade using the following scale:
>=93 -> A
90-93 -> A-
87-89 -> B+
83-86 -> B
80-82 -> B-
77-79 -> C+
73-76 -> C
70-72 -> C-
66-69 -> D+
60-65 -> D
<59 -> F
"""

sumGrades = 0.0
numEntries = 0
while True:
    userInput = input("Enter a grade! Or enter compute to calculate your average: ")
    if userInput == "compute":
        break
    else:
        sumGrades += float(userInput)
        numEntries += 1

if numEntries == 0:
    print("uh-oh! no grades entered")
else:
    average = sumGrades / numEntries
    print("Your grade average is:", average)
    #compute letter grade (important note-- you can only take one branch of an if/elif/else statement)
    letterGrade = ""
    if average >= 93:
        letterGrade = "A"
    elif average >= 90:
        letterGrade = "A-"
    elif average >= 87:
        letterGrade = "B+"
    elif average >= 83:
        letterGrade = "B"
    elif average >= 80:
        letterGrade = "B-"
    elif average >= 77:
        letterGrade = "C+"
    elif average >= 73:
        letterGrade = "C"
    elif average >= 70:
        letterGrade = "C"
    elif average >= 66:
        letterGrade = "D+"
    elif average >= 60:
        letterGrade = "D"
    else:
        letterGrade = "F"
    print("Your letter grade is:", letterGrade)