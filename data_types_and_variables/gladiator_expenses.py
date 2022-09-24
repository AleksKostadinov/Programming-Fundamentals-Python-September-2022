lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmet_count = 0
broken_sword_count = 0
broken_shield_count = 0
broken_armor_count = 0

for lost_fight in range(1, lost_fights + 1):

    if lost_fight % 2 == 0:
        broken_helmet_count += 1

    if lost_fight % 3 == 0:
        broken_sword_count += 1

    if lost_fight % 6 == 0:
        broken_shield_count += 1
        if broken_shield_count % 2 == 0:
            broken_armor_count += 1

expenses = helmet_price * broken_helmet_count + sword_price * broken_sword_count\
              + shield_price * broken_shield_count + armor_price * broken_armor_count

print(f"Gladiator expenses: {expenses:.2f} aureus")