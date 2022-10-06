product = input()
quantity = int(input())
price = 0


def price_calculator(type_product, number_quantity, cash):
    if type_product == 'coffee':
        cash = 1.5
    elif type_product == 'coke':
        cash = 1.4
    elif type_product == 'water':
        cash = 1
    elif type_product == 'snacks':
        cash = 2
    result = number_quantity * cash
    return f'{result:.2f}'


print(price_calculator(product, quantity, price))
