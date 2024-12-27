student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for student, score in student_scores.items():
    grade = ""

    if score <= 100 and score >= 91:
        grade = "Outstanding"
    elif score < 91 and score >= 81:
        grade = "Exceeds Expectations"
    elif score < 81 and score >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"

    student_grades[student] = grade

print(student_grades)