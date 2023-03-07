# question3
name = input("what is your name?")
labGrade = float(input("what is your lab grade ?"))
midTerm = float(input("what is your midterm grade?"))
finalGrade = float(input("what is your Final exam grade?"))
lastScore = (0.25 * labGrade) + (0.35 * midTerm) + (0.4 * finalGrade)
print("Name: " + name)
print("Lab: " + str(labGrade))
print("Midterm: " + str(midTerm))
print("Final: " + str(finalGrade))
print("your last score is : " + str(lastScore))

