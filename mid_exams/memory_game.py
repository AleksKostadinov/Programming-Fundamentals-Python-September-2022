list_of_elements = input().split()
first_index = 0
second_index = 0
counter = 0
win_flag = False
while True:
    if not list_of_elements:
        win_flag = True
        break
    command = input()

    if command == 'end':
        break
        
    command = list(map(int, command.split()))
    command = sorted(command, reverse=True)
    first_index = command[0]
    second_index = command[1]
    counter += 1

    if first_index == second_index or first_index < 0 or second_index < 0 or first_index >= len(
            list_of_elements) or second_index >= len(list_of_elements):
        position = len(list_of_elements) // 2
        list_of_elements.insert(position, f'-{counter}a')
        list_of_elements.insert(position + 1, f'-{counter}a')
        print("Invalid input! Adding additional elements to the board")
    elif list_of_elements[first_index] == list_of_elements[second_index]:
        print(f"Congrats! You have found matching elements - {list_of_elements[first_index]}!")
        del list_of_elements[first_index]
        del list_of_elements[second_index]
    elif list_of_elements[first_index] != list_of_elements[second_index]:
        print(f"Try again!")

if win_flag:
    print(f"You have won in {counter} turns!")
else:
    print("Sorry you lose :(")
    print(*list_of_elements)
