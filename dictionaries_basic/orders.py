command = input()
product_dict = {}
last_price = {}
while command != 'buy':
    name, price, quantity = command.split()
    product_dict[name] = product_dict.get(name, 0)
    product_dict[name] += int(quantity)
    last_price[name] = last_price.get(name, 0)
    last_price[name] = float(price)
    command = input()
for key, value in product_dict.items():
    if key in last_price:
        total_price = last_price[key] * value
        print(f'{key} -> {total_price:.2f}')
