line = input()
new_char = ''
for char in line:
    new_char += chr(ord(char) + 3)
print(new_char)