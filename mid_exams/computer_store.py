command = input()
total_without = 0

while command != 'special' and command != 'regular':
    price = float(command)
    if price < 0:
        print('Invalid price!')
        command = input()
        continue
    total_without += price
    command = input()
taxes = total_without * 0.2
total = total_without + taxes

if command == 'special':
    total *= 0.9
if total_without == 0:
    print('Invalid order!')
else:
    print(f'Congratulations you\'ve just bought a new computer!')
    print(f'Price without taxes: {total_without:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {total:.2f}$')
