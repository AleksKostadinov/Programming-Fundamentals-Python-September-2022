number_commands = int(input())
houses = list(map(int, input().split()))
current_position = 0
for num in range(number_commands):
    commands_list = input().split()
    command = commands_list[0]
    action = int(commands_list[1])
    if command == 'Forward':
        if action + current_position in range(len(houses)):
            current_position += action
            houses.pop(current_position)
    elif command == 'Back':
        if current_position - action in range(len(houses)):
            current_position -= action
            houses.pop(current_position)
    elif command == 'Gift' and action in range(len(houses)):
        current_position = action
        index, value = int(commands_list[1]), int(commands_list[2])
        if 1 <= value <= 500:
            houses.insert(action, value)
    elif command == 'Swap':
        value_2 = int(commands_list[2])
        if action in houses and value_2 in houses:
            index_1 = houses.index(action)
            index_2 = houses.index(value_2)
            houses[index_1], houses[index_2] = houses[index_2], houses[index_1]
print(f'Position: {current_position}')
print(', '.join(map(str, houses)))
