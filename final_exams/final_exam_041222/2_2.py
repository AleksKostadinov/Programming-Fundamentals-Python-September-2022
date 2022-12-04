import re

number = int(input())

for i in range(number):
    text = input()
    pattern = r'\|([A-Z]{4,})\|:#([A-Za-z]+ [A-Za-z]+)#'
    matches = re.search(pattern, text)

    if matches:
        print(f'{matches.group(1)}, The {matches.group(2)}')
        print(f'>> Strength: {len(matches.group(1))}')
        print(f'>> Armor: {len(matches.group(2))}')
    else:
        print("Access denied!")
