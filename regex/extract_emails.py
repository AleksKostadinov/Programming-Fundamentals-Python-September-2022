import re

text = input()
pattern = r'(^|(?<=\s)[a-z0-9]+)[\-_.]?([a-z0-9]+)?@(([a-z0-9]+)[\-_.])+[a-z0-9]+\b'
matches = re.finditer(pattern, text)
for match in matches:
    print(match.group())
