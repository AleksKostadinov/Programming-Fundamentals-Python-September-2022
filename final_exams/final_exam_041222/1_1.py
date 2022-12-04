def translate(other_, text_):
    char_, replacement_ = other_
    if char_ in text_:
        text_ = text_.replace(char_, replacement_)
        return text_
    return text_


def includes(other_, text_):
    substring = other_[0]
    if substring in text_:
        return True
    return False


def start(other_, text_):
    substring = other_[0]
    if text_.startswith(substring):
        return True
    return False


def lowercase(text_):
    text_ = text_.lower()
    return text_


def find_index(other_, text_):
    char_ = other_[0]
    if char_ in text_:
        char_index = text_.rfind(char_)
        return f'{char_index}'


def remove(other_, text_):
    start_index, count = int(other_[0]), int(other_[1])
    if start_index < len(text_) and count < len(text_):
        text_ = text_[:start_index] + text_[start_index + count:]
        return text_


text = input()
command = input()

while command != 'End':
    action, *other = command.split()
    if action == 'Translate':
        text = translate(other, text)
        print(text)
    elif action == 'Includes':
        print(includes(other, text))
    elif action == 'Start':
        print(start(other, text))
    elif action == 'Lowercase':
        text = lowercase(text)
        print(text)
    elif action == 'FindIndex':
        print(find_index(other, text))
    elif action == 'Remove':
        text = remove(other, text)
        print(text)

    command = input()
