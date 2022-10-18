def add_func(sequence):
    if lesson not in sequence:
        sequence.append(lesson)


def insert_func(sequence, indexes):
    if lesson not in sequence:
        sequence.insert(indexes, lesson)


def remove_func(sequence):
    if lesson in sequence:
        if exercise in sequence:
            sequence.remove(exercise)
        sequence.remove(lesson)


def swap_func(sequence, swapped):
    if lesson in sequence and swapped in sequence:
        lesson1_index = sequence.index(lesson)
        lesson2_index = sequence.index(swapped)
        sequence[lesson1_index], sequence[lesson2_index] = swapped, lesson

        if exercise in sequence:
            sequence.remove(exercise)
            lesson_index = sequence.index(lesson)
            sequence.insert(lesson_index + 1, exercise)

        if exercise_to_swap in sequence:
            sequence.remove(exercise_to_swap)
            lesson2_index = sequence.index(swapped)
            sequence.insert(lesson2_index + 1, exercise_to_swap)


def exercise_func(sequence):
    if lesson not in sequence:
        sequence.append(lesson)
        sequence.append(exercise)
    else:
        if exercise not in sequence:
            lesson_index = sequence.index(lesson)
            sequence.insert(lesson_index + 1, exercise)


schedule = input().split(', ')
command = input()

while command != 'course start':
    command = command.split(':')
    action = command[0]
    lesson = command[1]
    exercise = f"{lesson}-Exercise"

    if action == 'Add':
        add_func(schedule)
    elif action == 'Insert':
        index = int(command[2])
        insert_func(schedule, index)
    elif action == 'Remove':
        remove_func(schedule)
    elif action == 'Swap':
        swap = command[2]
        exercise_to_swap = f"{swap}-Exercise"
        swap_func(schedule, swap)
    elif action == "Exercise":
        exercise_func(schedule)
    command = input()

for num in range(len(schedule)):
    print(f"{num + 1}.{schedule[num]}")