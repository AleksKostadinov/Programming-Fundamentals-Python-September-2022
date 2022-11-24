text = input()
command = input()
while command != 'Reveal':
    command = command.split(":|:")
    action = command[0]
    if action == 'InsertSpace':
        index = int(command[1])
        text = text[:index] + ' ' + text[index:]
        print(text)
    elif action == 'Reverse':
        substring = command[1]
        if substring in text:
            text = text.replace(substring, '', 1)
            text = text + substring[::-1]
            print(text)
        else:
            print('error')
    elif action == 'ChangeAll':
        old_text, new_text = command[1], command[2]
        text = text.replace(old_text, new_text)
        print(text)
    command = input()
print(f'You have a new text message: {text}')
