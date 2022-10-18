food_kilo = float(input()) * 1000
hay_kilo = float(input()) * 1000
cover_kilo = float(input()) * 1000
pig_weight = float(input()) * 1000
flag = False
for day in range(1, 31):
    food_kilo -= 300
    if day % 2 == 0:
        hay_kilo -= food_kilo * 0.05
    if day % 3 == 0:
        cover_kilo -= 1 / 3 * pig_weight
    if food_kilo < 0 or hay_kilo < 0 or cover_kilo < 0:
        flag = True
        break
if flag:
    print(f'Merry must go to the pet store!')
else:
    food, hay, cover = food_kilo / 1000, hay_kilo / 1000, cover_kilo / 1000
    print(f'Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.')
