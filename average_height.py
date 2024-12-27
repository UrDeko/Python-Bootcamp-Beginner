def average_student_height(student_heights):
    result = 0

    for height in student_heights:
        result += height

    result = round(result / len(student_heights), 2)
    return result

if __name__ == "__main__":
    print(average_student_height([180, 124, 165, 173, 189, 169, 146]))