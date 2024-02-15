try:
    score = float(input("Enter a score between 0.0 and 1.0: "))
except ValueError:
    print("Error: Please enter a numeric value.")
    exit()

if 0.0 <= score <= 1.0:
    grades = [(0.9, 'A'), (0.8, 'B'), (0.7, 'C'), (0.6, 'D')]
    for grade_score, grade in grades:
        if score >= grade_score:
            print(f"Grade: {grade}")
            break
    else:
        print("Grade: F")
else:
    print("Error: Score is out of range.")