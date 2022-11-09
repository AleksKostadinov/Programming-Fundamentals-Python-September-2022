def digit(words: str):
    return [int(x) for x in words if x.isdigit()]


def char(words: str):
    return [x for x in words if x.isalpha()]


def other(words: str):
    return [x for x in words if not x.isalnum()]


word = input()
digits = digit(word)
chars = char(word)
others = other(word)

print(*digits, sep='')
print(*chars, sep='')
print(*others, sep='')
