def char_to_string(first, second):
    result = []
    for char in range(ord(first) + 1, ord(second)):
        result.append(chr(char))
    return f"{' '.join(result)}"


first_char = input()
second_char = input()

print(char_to_string(first_char, second_char))