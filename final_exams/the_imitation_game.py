encrypted = input()
command = input()

while command != 'Decode':
    command_list = command.split('|')
    action = command_list[0]
    if action == 'ChangeAll':
        replacement = command_list[1]
        substring = command_list[2]
        encrypted = encrypted.replace(replacement, substring)
    elif action == 'Insert':
        index = int(command_list[1])
        value = command_list[2]
        encrypted = encrypted[:index] + value + encrypted[index:]
    elif action == 'Move':
        index = int(command_list[1])
        if len(encrypted) > index:
            encrypted = encrypted[index:] + encrypted[:index]
    command = input()
print(f'The decrypted message is: {encrypted}')
