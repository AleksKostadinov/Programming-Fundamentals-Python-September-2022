text = input()
command = input()

while command != 'End':
    command_type = command.split()
    action = command_type[0]
    if action == 'Translate':
        char = command_type[1]
        replacement = command_type[2]
        if char in text:
            text = text.replace(char, replacement)
            print(text)
        else:
            print(text)
    elif action == 'Includes':
        substring = command_type[1]
        if substring in text:
            print('True')
        else:
            print('False')
    elif action == 'Start':
        substring = command_type[1]
        if text.startswith(substring):
            print('True')
        else:
            print('False')
    elif action == 'Lowercase':
        text = text.lower()
        print(text)
    elif action == 'FindIndex':
        char = command_type[1]
        if char in text:
            char_index = text.rfind(char)
            print(char_index)
    elif action == 'Remove':
        start_index = int(command_type[1])
        count = int(command_type[2])
        if start_index < len(text) and count < len(text):
            text = text[:start_index] + text[start_index + count:]
            print(text)
    command = input()
