number_ingredients = int(input())

calories = 0

for i in range(number_ingredients):
    ingredients = input().lower()
    if ingredients == 'cheese':
        calories += 500

    if ingredients == 'tomato sauce':
        calories += 150

    if ingredients == 'salami':
        calories += 600

    if ingredients == 'pepper':
        calories += 50

print(f'Total calories: {calories}')

