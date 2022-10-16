secret_message = input().split()
decipher_message = []
for word in secret_message:
    digit_list = ''
    word_list = []
    for char in word:
        if char.isdigit():
            digit_list += char
        else:
            word_list += char
    decipher_message.append(chr(int(digit_list)))
    word_list[0], word_list[-1] = word_list[-1], word_list[0]
    decipher_message += word_list
    decipher_message += ' '

print(''.join(decipher_message))
