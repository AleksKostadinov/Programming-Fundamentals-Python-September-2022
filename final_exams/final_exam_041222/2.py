import re

number = int(input())

for i in range(number):
    text = input()
    boss_pattern = r'(|)+([A-Z]{4,})\1'
    title_pattern = r':(#)([A-Za-z]+\s[A-Za-z]+)\1'
    boss_match = re.search(boss_pattern, text)
    title_match = re.search(title_pattern, text)

    if boss_match and title_match:
        print(f'{boss_match.group(2)}, The {title_match.group(2)}')
        print(f'>> Strength: {len(boss_match.group(2))}')
        print(f'>> Armor: {len(title_match.group(2))}')
    else:
        print("Access denied!")