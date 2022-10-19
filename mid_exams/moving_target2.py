def shoot_func(sequence):
    if 0 <= index < len(sequence):
        if sequence[index] > power:
            sequence[index] -= power
        elif sequence[index] <= power:
            sequence.pop(index)
    return sequence


def add_func(sequence):
    if 0 <= index < len(sequence):
        sequence.insert(index, power)
    else:
        print("Invalid placement!")
    return sequence


def strike_func(sequence):
    if index + power >= len(sequence) or ((index - power) < 0):
        print("Strike missed!")
    else:
        sequence = sequence[: index - power] + sequence[index + power + 1:]
    return sequence


sequence_list = list(map(int, input().split()))
command = input()
while command != 'End':
    command_list = command.split()
    action = command_list[0]
    index = int(command_list[1])
    power = int(command_list[2])
    if action == 'Shoot':
        shoot_func(sequence_list)
    elif action == 'Add':
        add_func(sequence_list)
    elif action == 'Strike':
        sequence_list = strike_func(sequence_list)
    command = input()
print('|'.join(map(str, sequence_list)))
