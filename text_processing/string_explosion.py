line = input()
result = ''
char_index = 0
for index, char in enumerate(line):
    if char == '>':
        char_index += int(line[index + 1])
        result += char
    else:
        if char_index != 0:
            char_index -= 1
        else:
            result += char
print(result)
