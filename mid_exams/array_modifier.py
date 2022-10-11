list_of_numbers = [int(x) for x in input().split()]

while True:
    command = input().split()
    if command[0] == 'decrease':
        for i, d in enumerate(list_of_numbers):
            list_of_numbers.pop(i)
            list_of_numbers.insert(i, d-1)
    elif command[0] == 'end':
        break
    else:
        index_1 = int(command[1])
        index_2 = int(command[2])
        if command[0] == 'swap':
            list_of_numbers[index_1], list_of_numbers[index_2] = list_of_numbers[index_2], list_of_numbers[index_1]
        elif command[0] == 'multiply':
            list_of_numbers[index_1] *= list_of_numbers[index_2]
print(', '.join(map(str, list_of_numbers)))
