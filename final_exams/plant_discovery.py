number_lines = int(input())
plants_dict = {}

for number in range(number_lines):
    plant, rarity = input().split('<->')
    if plant not in plants_dict:
        plants_dict[plant] = 0
    plants_dict[plant] = {"Rarity": int(rarity), "Rating": []}

command = input()
while command != 'Exhibition':
    action, other = command.split(': ')
    if action == 'Rate':
        plant, rating = other.split(' - ')
        if plant not in plants_dict.keys():
            print("error")
        else:
            plants_dict[plant]['Rating'].append(int(rating))
    elif action == 'Update':
        plant, new_rarity = other.split(' - ')
        if plant not in plants_dict.keys():
            print("error")
        else:
            plants_dict[plant]['Rarity'] = int(new_rarity)
    elif action == 'Reset':
        plant = other
        if plant not in plants_dict.keys():
            print("error")
        else:
            plants_dict[plant]["Rating"] = []
    command = input()
print('Plants for the exhibition:')
for plant in plants_dict:
    if plants_dict[plant]['Rating']:
        average_rating = sum(plants_dict[plant]['Rating']) / len(plants_dict[plant]['Rating'])
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {plants_dict[plant]['Rarity']}; Rating: {average_rating:.2f}")
