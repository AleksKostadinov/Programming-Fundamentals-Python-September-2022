count = int(input())
result = ''
for i in range(count):
    text_message = int(input())
    if text_message == 0:
        result += ' '
    else:
        length = len(str(text_message))
        main_digit = text_message % 10
        start_index = (main_digit - 2) * 3

        if main_digit == 8 or main_digit == 9:
            start_index += 1

        letter_index = start_index + length - 1
        result += chr(97 + letter_index)

print(result)