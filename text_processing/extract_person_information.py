number_lines = int(input())
for number_line in range(number_lines):
    lines = input().split()
    lst_name, lst_age = [], []
    for line in lines:
        is_flag_name = False
        is_flag_age = False
        for index, char in enumerate(line):
            if char == '@':
                is_flag_name = True
            if is_flag_name:
                lst_name.append(line[index])
            if char == '|':
                lst_name = [value for value in lst_name if value != '@']
                lst_name = [value for value in lst_name if value != '|']
                is_flag_name = False
            if char == '#':
                is_flag_age = True
            if is_flag_age:
                lst_age.append(line[index])
            if char == '*':
                lst_age = [value for value in lst_age if value != '#']
                lst_age = [value for value in lst_age if value != '*']
                is_flag_age = False
    print(f"{''.join(lst_name)} is {''.join(lst_age)} years old.")
