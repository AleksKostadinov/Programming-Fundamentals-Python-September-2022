line = input()
new_char, current_char = '', ''
for char in line:
    if char != current_char:
        new_char += char
        current_char = char
print(new_char)
