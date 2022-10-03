list_of_numbers = input().split()
list_of_strings = input().split()

sum_index = 0
counter = 0
string_to_list = True

for numbers in list_of_numbers:
    char_found = False
    for number in str(numbers):
        sum_index += int(number)

    if string_to_list:
        list_of_strings = ' '.join(list_of_strings)
        string_to_list = False
        counter = len(list_of_strings)

    if sum_index >= counter:
        while True:
            for index, searched_string in enumerate(list_of_strings):
                if sum_index == index:
                    print(searched_string, end='')
                    list_of_strings = list_of_strings.replace(searched_string, '', 1)
                    counter = len(list_of_strings)
                    char_found = True
                    break
            sum_index -= counter
            if char_found:
                sum_index = 0
                break
    else:
        for index, searched_string in enumerate(list_of_strings):
            if sum_index == index:
                print(searched_string, end='')
                list_of_strings = list_of_strings.replace(searched_string, '', 1)
                counter = len(list_of_strings)
                sum_index = 0
                break

