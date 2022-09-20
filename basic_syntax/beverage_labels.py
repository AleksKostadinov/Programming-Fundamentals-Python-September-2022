product_name = input()
volume = int(input())
energy_100ml = int(input())
sugar_100g = int(input())
energy = (volume / 100) * energy_100ml
sugar = (volume / 100) * sugar_100g

print(f"{volume}ml {product_name}:")
print(f'{energy:.2f}kcal, {sugar:.2f}g sugars')
