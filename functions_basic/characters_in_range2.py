def char_to_string(first, second):
    characters = []
    for char in range(ord(first) + 1, ord(second)):
        characters += chr(char)
    return characters


first_char = input()
second_char = input()

result = char_to_string(first_char, second_char)
print(*result)
