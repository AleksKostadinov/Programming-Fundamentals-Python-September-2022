import re

command = input()
names = []
total_price = 0

while command != 'Purchase':
    pattern = r'>>([a-zA-Z]+)<<([0-9]+?\.?[0-9]+?)!([0-9]+)\b'
    matches = re.finditer(pattern, command)
    for match in matches:
        names.append(match.group(1))
        total_price += float(match.group(2)) * int(match.group(3))

    command = input()
print('Bought furniture:')
for i in range(len(names)):
    print(names[i])
print(f'Total money spend: {total_price:.2f}')
