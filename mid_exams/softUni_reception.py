first_employer_vol = int(input())
second_employer_vol = int(input())
third_employer_vol = int(input())
students = int(input())
hours = 0
while students > 0:
    students -= first_employer_vol + second_employer_vol + third_employer_vol
    hours += 1
    if hours % 4 == 0:
        hours += 1
print(f'Time needed: {hours}h.')