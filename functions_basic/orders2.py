def price_calculator(product, quantity):
    if product == 'coffee':
        return quantity * 1.5
    elif product == 'coke':
        return quantity * 1.4
    elif product == 'water':
        return quantity * 1
    elif product == 'snacks':
        return quantity * 2


product = input()
quantity = int(input())
print(f'{float(price_calculator(product, quantity)):.2f}')
