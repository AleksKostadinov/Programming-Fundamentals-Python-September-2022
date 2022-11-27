def cities_func(command_):
    command_list = command_.split('||')
    city, population, gold = command_list[0], int(command_list[1]), int(command_list[2])
    if city not in cities_info:
        cities_info[city] = {'population': 0, 'gold': 0}
    cities_info[city]['population'] += population
    cities_info[city]['gold'] += gold


def plunder_func(action_command_list_):
    city, people, gold = action_command_list_[1], int(action_command_list_[2]), int(action_command_list_[3])
    if people < cities_info[city]['population'] and gold < cities_info[city]['gold']:
        cities_info[city]['population'] -= people
        cities_info[city]['gold'] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
    elif people == cities_info[city]['population'] or gold == cities_info[city]['gold']:
        del cities_info[city]
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        print(f"{city} has been wiped off the map!")


def prosper_func(action_command_list_):
    city, gold = action_command_list_[1], int(action_command_list_[2])
    if gold < 0:
        print(f"Gold added cannot be a negative number!")
    else:
        cities_info[city]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {city} now has {cities_info[city]['gold']} gold.")


command = input()
cities_info = {}
while command != 'Sail':
    cities_func(command)
    command = input()
action_command = input()
while action_command != 'End':
    action_command_list = action_command.split('=>')
    action = action_command_list[0]
    if action == 'Plunder':
        plunder_func(action_command_list)
    elif action == 'Prosper':
        prosper_func(action_command_list)
    action_command = input()
if cities_info:
    print(f"Ahoy, Captain! There are {len(cities_info)} wealthy settlements to go to:")
    for cities, info in cities_info.items():
        print(f"{cities} -> Population: {cities_info[cities]['population']} citizens, "
              f"Gold: {cities_info[cities]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
