list_of_numbers = [int(number) for number in input().split()]
command_list = input().split()
command = command_list[0]

while command != 'end':
    string_command = command_list[-1]
    counter = 0
    max_number = []
    min_number = []
    first_counter = []
    last_counter = []
    if command == 'exchange':
        index_command = int(command_list[1])
        if index_command < 0 or index_command > len(list_of_numbers):
            print('Invalid index')
        list_of_numbers = list_of_numbers[index_command + 1:] + list_of_numbers[:index_command + 1]
    elif command == 'max':
        if string_command == 'even':
            for even in list_of_numbers:
                if even % 2 == 0:
                    max_number.append(even)
        elif string_command == 'odd':
            for odd in list_of_numbers:
                if odd % 2 != 0:
                    max_number.append(odd)
        if max_number:
            max_number = max(max_number)
            max_number = list_of_numbers.index(max_number)
            print(max_number)
        else:
            print("No matches")
    elif command == 'min':
        if string_command == 'even':
            for even in list_of_numbers:
                if even % 2 == 0:
                    min_number.append(even)
        elif string_command == 'odd':
            for odd in list_of_numbers:
                if odd % 2 != 0:
                    min_number.append(odd)
        if min_number:
            min_number = min(min_number)
            min_number = list_of_numbers.index(min_number)
            print(min_number)
        else:
            print("No matches")
    elif command == 'first':
        index_command = int(command_list[1])
        if string_command == 'even':
            for i in range(index_command):
                for even_counter in list_of_numbers:

                    if even_counter % 2 == 0:
                        counter += 1
                        if counter > index_command:
                            break
                        first_counter.append(even_counter)
                if index_command - len(list_of_numbers) > 0:
                    print('Invalid count')
                    break
                elif first_counter:
                    print(first_counter)
        elif string_command == 'odd':
            for odd_counter in list_of_numbers:
                if odd_counter % 2 != 0:
                    counter += 1
                    if counter > index_command:
                        break
                    first_counter.append(odd_counter)
            if first_counter:
                print(first_counter)
    elif command == 'last':
        index_command = int(command_list[1])
        if string_command == 'even':
            for even_counter in list_of_numbers:
                if even_counter % 2 == 0:
                    counter += 1
                    if counter > index_command:
                        print('Invalid count')
                        break
                    last_counter.append(even_counter)
        elif string_command == 'odd':
            for odd_counter in list_of_numbers:
                if odd_counter % 2 != 0:
                    counter += 1
                    if counter > index_command:
                        print('Invalid count')
                        break
                    last_counter.append(odd_counter)
        if last_counter:
            print(last_counter)
        else:
            print('[]')
    command_list = input().split()
    command = command_list[0]
print(list_of_numbers)
