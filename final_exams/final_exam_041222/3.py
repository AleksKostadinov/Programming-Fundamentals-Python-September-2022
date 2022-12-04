def enroll(hero_name_, collection_):
    if hero_name_ not in collection_:
        collection_[hero_name_] = []
    else:
        print(f"{hero_name_} is already enrolled.")


def learn(hero_name_, spell_, collection_):
    if hero_name_ not in collection_:
        print(f"{hero_name_} doesn't exist.")
    elif spell_ in collection_[hero_name_]:
        print(f"{hero_name_} has already learnt {spell_}.")
    else:
        collection_[hero_name_].append(spell_)


def unlearn(hero_name_, spell_, collection_):
    if hero_name_ not in collection_:
        print(f"{hero_name_} doesn't exist.")
    elif spell_ not in collection_[hero_name_]:
        print(f"{hero_name_} doesn't know {spell_}.")
    else:
        collection_[hero_name_].remove(spell_)


command = input()
collection = {}
while command != 'End':
    command_type = command.split()
    action, hero_name, spell = command_type[0], command_type[1], command_type[-1]
    if action == 'Enroll':
        enroll(hero_name, collection)
    elif action == 'Learn':
        learn(hero_name, spell, collection)
    elif action == 'Unlearn':
        unlearn(hero_name, spell, collection)
    command = input()

print('Heroes:')
for hero_name, spells in collection.items():
    print(f"== {hero_name}: {', '.join(spells)}")
