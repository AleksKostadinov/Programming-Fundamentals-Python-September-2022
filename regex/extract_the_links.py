import re

pattern = r'w{3}\.[a-zA-Z0-9\-]+\.[a-z\.]+'
text = input()

while text:
    matches = re.search(pattern, text)
    if matches:
        print(matches.group())
    text = input()
