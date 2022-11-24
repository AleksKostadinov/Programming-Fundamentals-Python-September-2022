import re

text = input()
pattern = r'([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

matches = re.finditer(pattern, text)
pairs = []
mirror_words = []
if matches:
    for match in matches:
        pairs.append(match.group(2))
        pairs.append(match.group(3))

for pair in range(0, len(pairs), 2):
    first_word, second_word = pairs[pair], pairs[pair + 1]
    if first_word == second_word[::-1]:
        mirror_words.append(f'{first_word} <=> {second_word}')

if pairs:
    print(f"{int(len(pairs)/2)} word pairs found!")
else:
    print("No word pairs found!")

if mirror_words:
    print(f'The mirror words are:')
    print(', '.join(mirror_words))
else:
    print(f"No mirror words!")
