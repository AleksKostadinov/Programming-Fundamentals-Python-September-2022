import re

text = input()
pattern = r"(:{2}|\*{2})([A-Z][a-z]{2,})\1"
matches = re.finditer(pattern, text)
emojis = []
cool_emojis = []
numbers_ = 1
if matches:
    for match in matches:
        emojis.append(match[0])

digits = [x for x in text if x.isdigit()]

for digit in digits:
    numbers_ *= int(digit)

for emoji in emojis:
    coolness = sum([ord(char) for char in emoji if char.isalpha()])
    if coolness > numbers_:
        cool_emojis.append(emoji)
print(f"Cool threshold: {numbers_}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
print('\n'.join(cool_emojis))