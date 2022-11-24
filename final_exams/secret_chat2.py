def insert_space(text_, command_):
    index = int(command_[1])
    text_ = text_[:index] + ' ' + text_[index:]
    print(text_)
    return text_


def reverse(text_, command_):
    substring = command_[1]
    if substring in text_:
        text_ = text_.replace(substring, '', 1)
        text_ = text_ + substring[::-1]
        print(text_)
        return text_
    print('error')
    return text_


def change_all(text_, command_):
    old_text, new_text = command_[1], command_[2]
    text_ = text_.replace(old_text, new_text)
    print(text_)
    return text_


text = input()
command = input()
while command != 'Reveal':
    command = command.split(":|:")
    action = command[0]
    if action == 'InsertSpace':
        text = insert_space(text, command)
    elif action == 'Reverse':
        text = reverse(text, command)
    elif action == 'ChangeAll':
        text = change_all(text, command)
    command = input()
print(f'You have a new text message: {text}')
