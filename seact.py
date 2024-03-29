def calculate_grade(score):
    if score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'

score = float(input("Enter a score between 0.0 and 1.0: "))
if 0.0 <= score <= 1.0:
    grade = calculate_grade(score)
    print("Grade:", grade)
else:
    print("Error: Score must be between 0.0 and 1.0.")
