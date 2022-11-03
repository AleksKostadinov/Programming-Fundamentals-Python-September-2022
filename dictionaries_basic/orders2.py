def product_func(names: str, quantities: int, product_dictionary: dict):
    product_dictionary[names] = product_dictionary.get(names, 0)
    product_dictionary[names] += int(quantities)
    return product_dictionary


def last_price_func(names: str, prices: float, last_prices: dict):
    last_prices[names] = last_prices.get(names, 0)
    last_prices[names] = float(prices)
    return last_prices


command = input()
product_dict = {}
last_price = {}
while command != 'buy':
    name, price, quantity = command.split()
    product_dict = product_func(name, quantity, product_dict)
    last_price = last_price_func(name, price, last_price)
    command = input()
for key, value in product_dict.items():
    if key in last_price:
        total_price = last_price[key] * value
        print(f'{key} -> {total_price:.2f}')
