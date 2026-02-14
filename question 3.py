"""
Question 8: Letter Grade using if conditions

This program:
1. Takes a class score from the user
2. Uses if-elif-else conditions
3. Prints the corresponding letter grade
"""
#take input
score = float(input("Enter your  score 0-100: "))

# check score using if-elif-else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Print grade
print("Your letter grade is:", grade)
