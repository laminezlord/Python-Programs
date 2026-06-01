score = float(input("Enter the student's score: "))
if score >= 70 and score <= 100:
    print("The student received an A")
elif score >= 60 and score < 70:
    print("The student received a B")
elif score >= 50 and score < 60:
    print("The student received a C")
elif score >= 45 and score < 50:
    print("The student received a D")
elif score <= 45:
     print("The student failed")
else :
    print("Invalid score. Please enter a score between 0 and 100.")
