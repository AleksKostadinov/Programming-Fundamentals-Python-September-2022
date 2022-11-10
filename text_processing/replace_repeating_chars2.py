line = input()
result = ''
for index, char in enumerate(line):
    if index == 0:
        result = char
    else:
        if char != result[-1]:
            result += char
print(result)
