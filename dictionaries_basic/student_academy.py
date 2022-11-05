pair_of_rows = int(input())
students_grades = {}
for row in range(pair_of_rows):
    student = input()
    grade = float(input())
    if student not in students_grades.keys():
        students_grades[student] = []
    students_grades[student].append(grade)
for student in students_grades.keys():
    avg_grade = sum(students_grades[student]) / len(students_grades[student])
    if avg_grade >= 4.5:
        print(f'{student} -> {avg_grade:.2f}')
    