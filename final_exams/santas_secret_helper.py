import re
key_number = int(input())
text = input()
while text != 'end':
    text_str = ''
    for char in text:
        text_str += chr(ord(char) - key_number)
    text = input()
    pattern = r"@([A-Za-z]+)[^@\-!:>]*!([G])!"
    matches = re.findall(pattern, text_str)
    if matches:
        for match in matches:
            print(match[0])
