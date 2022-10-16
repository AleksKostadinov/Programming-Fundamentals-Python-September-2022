numbers_list = list(map(int, input().split(', ')))
boundary = 0
max_number = max(numbers_list)
while boundary < max_number:
    group_list = []
    boundary += 10
    for value in numbers_list:
        if (boundary - 10) < value <= boundary:
            group_list.append(value)
    print(f"Group of {boundary}'s: {group_list}")
