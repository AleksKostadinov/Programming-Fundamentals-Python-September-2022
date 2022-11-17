import re

result = []
text = input()
pattern = r'\b_{1}[a-zA-Z]+\b'
matches = re.findall(pattern, text)
for match in matches:
    result.append(match.strip('_'))
print(','.join(result))
