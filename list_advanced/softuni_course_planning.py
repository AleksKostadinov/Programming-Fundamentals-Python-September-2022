schedule = input().split(', ')
command = input()


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


def swap_func(sequence,):
    pass


def exercise_func(sequence, ):
    pass


while command != 'course start':
    command_list = command.split(':')
    action = command[0]
    lesson = command[1]
    exercise = f"{lesson}-Exercise"

    if action == 'Add':
        add_func(schedule)
    elif action == 'Insert':
        index = command[2]
        insert_func(schedule, index)
    elif action == 'Remove':
        pass
    elif action == 'Swap':
        pass
    command = input()
