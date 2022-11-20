import re

foods = input()
total_calories = 0
food_list = []
pattern = r'(\||#)([a-zA-Z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,4}|10000)\1'
match = re.findall(pattern, foods)
if match:
    for product in match:
        name = product[1]
        food_list.append(name)
        date = product[2]
        food_list.append(date)
        calories = int(product[3])
        food_list.append(calories)
        total_calories += calories
days_last = total_calories // 2000
print(f'You have food to last you for: {days_last} days!')
for item in range(0, len(food_list), 3):
    print(f'Item: {food_list[item]}, Best before: {food_list[item+1]}, Nutrition: {food_list[item+2]}')
