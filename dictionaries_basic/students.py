info = input()
students = {}
while ":" in info:
    name, student_id, student_course = info.split(':')
    students[name] = student_id, student_course

    info = input()

course = info.replace('_', ' ')

for key, value in students.items():
    student_id = value[0]
    student_course = value[1]
    if student_course == course:
        print(f'{key} - {student_id}')

