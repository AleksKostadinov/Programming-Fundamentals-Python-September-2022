def change_all(encrypted_, command_list_):
    replacement = command_list_[1]
    substring = command_list_[2]
    encrypted_ = encrypted_.replace(replacement, substring)
    return encrypted_


def insert(encrypted_, command_list_):
    index = int(command_list_[1])
    value = command_list_[2]
    encrypted_ = encrypted_[:index] + value + encrypted_[index:]
    return encrypted_


def move(encrypted_, command_list_):
    index = int(command_list_[1])
    if len(encrypted_) > index:
        encrypted_ = encrypted_[index:] + encrypted_[:index]
    return encrypted_


encrypted = input()
command = input()

while command != 'Decode':
    command_list = command.split('|')
    action = command_list[0]
    if action == 'ChangeAll':
        encrypted = change_all(encrypted, command_list)
    elif action == 'Insert':
        encrypted = insert(encrypted, command_list)
    elif action == 'Move':
        encrypted = move(encrypted, command_list)
    command = input()
print(f'The decrypted message is: {encrypted}')
