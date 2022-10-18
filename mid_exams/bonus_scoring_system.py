number_students = int(input())
number_lectures = int(input())
bonus = int(input())
total_bonus_list = []
attendance_list = []
if number_lectures == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
else:
    for student in range(number_students):
        attendance = int(input())
        total_bonus = round((attendance / number_lectures) * (5 + bonus))
        total_bonus_list.append(total_bonus)
        attendance_list.append(attendance)
    print(f'Max Bonus: {max(total_bonus_list)}.')
    print(f'The student has attended {max(attendance_list)} lectures.')