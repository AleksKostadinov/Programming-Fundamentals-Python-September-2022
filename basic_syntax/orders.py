number_of_orders = int(input())
total = 0
for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if 0.01 > price_per_capsule or price_per_capsule > 100:
        continue
    if 1 > days or days > 31:
        continue
    if 1 > capsules or capsules > 2000:
        continue

    price = price_per_capsule * days * capsules
    total += price

    print(f"The price for the coffee is: ${price:.2f}")
print(f'Total: ${total:.2f}')
