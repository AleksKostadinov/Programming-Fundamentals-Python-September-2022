import re

pattern = r'\d+'
text = input()
result = []

while text:
    matches = re.findall(pattern, text)
    result += matches
    text = input()

print(' '.join(result))
