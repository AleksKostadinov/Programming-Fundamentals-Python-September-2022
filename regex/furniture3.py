import re

command = input()
total_price = 0
pattern = r'>>([a-zA-Z]+)<<([0-9]+[\.0-9]*)!([0-9]+)\b'

print('Bought furniture:')

while command != 'Purchase':
    matches = re.search(pattern, command)
    if matches:
        furniture, price, quantity = matches.groups()
        total_price += float(price) * int(quantity)
        print(furniture)
    command = input()

print(f'Total money spend: {total_price:.2f}')
