command = input()
while command != 'end':
    text = ''
    for char in reversed(command):
        text += char
    print(command + ' = ' + text)
    command = input()
    