import re

command = input()
total_price = 0
pattern = r'>>(?P<furniture>[a-zA-Z]+)<<(?P<price>[0-9]+[\.0-9]*)!(?P<quantity>[0-9]+)'

print('Bought furniture:')

while command != 'Purchase':
    matches = re.finditer(pattern, command)
    for match in matches:
        total_price += float(match['price']) * int(match['quantity'])
        print(match['furniture'])
    command = input()

print(f'Total money spend: {total_price:.2f}')
