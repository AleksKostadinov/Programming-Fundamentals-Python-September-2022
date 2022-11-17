import re

pattern = r'[0-9]+'

while True:
    text = input()
    if text:
        matches = re.findall(pattern, text)
        for match in matches:
            print((''.join(match)), end=' ')
    else:
        break
