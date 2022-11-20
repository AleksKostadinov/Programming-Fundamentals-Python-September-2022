import re

foods = input()
total_calories = 0
food_list = []
pattern = r'(\||#)([a-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,4}|10000)\1'
match = re.findall(pattern, foods)
if match:
    for product in match:
        name, date, calories = product[1], product[2], int(product[3])
        food_list.append({name: [date, calories]})
        total_calories += calories
days_last = total_calories // 2000
print(f'You have food to last you for: {days_last} days!')
for product in food_list:
    for key, value in product.items():
        print(f'Item: {key}, Best before: {value[0]}, Nutrition: {value[1]}')
