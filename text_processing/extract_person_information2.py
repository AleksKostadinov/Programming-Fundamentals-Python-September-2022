number_lines = int(input())

for line in range(number_lines):
    lines = input()
    name, age = "", ""
    name_start_index, name_end_index, age_start_index, age_end_index = 0, 0, 0, 0
    for index, character in enumerate(lines):
        if character == "@":
            name_start_index = index + 1
        if character == "|":
            name_end_index = index

        if character == "#":
            age_start_index = index + 1
        if character == "*":
            age_end_index = index

    name = lines[name_start_index:name_end_index]
    age = lines[age_start_index:age_end_index]
    print(f"{name} is {age} years old.")