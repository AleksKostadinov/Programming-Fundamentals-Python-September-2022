budget = float(input())
num_items = int(input())
total_price = 0

for item in range(num_items):
    name = input()
    price = float(input())
    count = int(input())
    if count > 1:
        name += 's'

    print(f'Adding {count} {name} to cart.')
    total_price += price * count
    budget -= price * count
print(f'Subtotal: ${total_price:.2f}')
if budget >= 0:
    print(f'Money left: ${budget:.2f}')
else:
    print(f'Not enough. We need ${abs(budget):.2f} more.')
