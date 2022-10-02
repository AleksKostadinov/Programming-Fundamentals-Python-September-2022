items = input().split('|')
budget = float(input())

bought_items_price = []
profit = 0
for item in items:
    list_items = item.split('->')
    price = float(list_items[1])
    if 'Clothes' in list_items and price <= 50.00 or \
            'Shoes' in list_items and price <= 35.00 or \
            'Accessories' in list_items and price <= 20.50:
        if price <= budget:
            budget -= price
            bought_items_price.append(price)

for price in bought_items_price:
    profit += price * 0.4
    sell_price = price * 1.40
    budget += sell_price
    print(f'{sell_price:.2f}', end=' ')

print(f'\nProfit: {profit:.2f}')

if budget >= 150:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')
