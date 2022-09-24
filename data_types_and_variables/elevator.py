number_of_people = int(input())
capacity = int(input())

course = 0
full_course = number_of_people // capacity
not_full_course = number_of_people % capacity

if not_full_course:
    course = 1

total_courses = full_course + course

print(total_courses)
