number_dragons = int(input())
dragons = {}
for number in range(number_dragons):
    color, name, damage, health, armor = input().split()
    if damage == 'null':
        dragon_damage = 45
    else:
        dragon_damage = int(damage)
    if health == 'null':
        dragon_health = 250
    else:
        dragon_health = int(health)
    if armor == 'null':
        dragon_armor = 10
    else:
        dragon_armor = int(armor)
    if color not in dragons:
        dragons[color] = {name: []}
        dragons[color][name].append(dragon_damage)
        dragons[color][name].append(dragon_health)
        dragons[color][name].append(dragon_armor)
    else:
        dragons[color].update({name: []})
        dragons[color][name].append(dragon_damage)
        dragons[color][name].append(dragon_health)
        dragons[color][name].append(dragon_armor)
for color, dragon in dragons.items():
    damage_ = 0
    health_ = 0
    armor_ = 0
    for names, specs in dragon.items():
        damage_ += specs[0]/len(dragon)
        health_ += specs[1]/len(dragon)
        armor_ += specs[2]/len(dragon)
    print(f'{color}::({damage_:.2f}/{health_:.2f}/{armor_:.2f})')
    for names, specs in sorted(dragon.items()):
        damage = specs[0]
        health = specs[1]
        armor = specs[2]
        print(f'-{names} -> damage: {damage}, health: {health}, armor: {armor}')
