number_wagons = int(input())
wagons = [0] * number_wagons

while True:
    command = input()
    if command == 'End':
        break
    split_command = command.split()
    if split_command[0] == 'add':
        add_people = int(split_command[1])
        wagons[-1] += add_people
    elif split_command[0] == 'insert':
        index = int(split_command[1])
        add_people = int(split_command[2])
        wagons[index] += add_people
    elif split_command[0] == 'leave':
        index = int(split_command[1])
        remove_people = int(split_command[2])
        wagons[index] -= remove_people
print(wagons)
