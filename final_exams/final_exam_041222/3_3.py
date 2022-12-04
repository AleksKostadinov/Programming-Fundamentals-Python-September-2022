command = input()
collection = {}

while command != 'End':
    command_type = command.split()
    action, hero_name, spell = command_type[0], command_type[1], command_type[-1]

    if action == 'Enroll':
        if hero_name not in collection:
            collection[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")

    elif action == 'Learn':
        if hero_name not in collection:
            print(f"{hero_name} doesn't exist.")
        elif spell in collection[hero_name]:
            print(f"{hero_name} has already learnt {spell}.")
        else:
            collection[hero_name].append(spell)

    elif action == 'Unlearn':
        if hero_name not in collection:
            print(f"{hero_name} doesn't exist.")
        elif spell not in collection[hero_name]:
            print(f"{hero_name} doesn't know {spell}.")
        else:
            collection[hero_name].remove(spell)

    command = input()

print("Heroes:")
for hero_name, spells in collection.items():
    print(f"== {hero_name}: {', '.join(spells)}")