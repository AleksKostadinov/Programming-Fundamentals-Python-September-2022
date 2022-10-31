characters = input().strip()
char_dict = {}
char = ''
for char in characters:
    if char not in char_dict:
        if char == ' ':
            continue
        char_dict[char] = 0
    char_dict[char] += 1
for key, value in char_dict.items():
    print(f'{key} -> {value}')
