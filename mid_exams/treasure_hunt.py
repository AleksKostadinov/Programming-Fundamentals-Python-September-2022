loot = input().split('|')
command = input()

while command != 'Yohoho!':
    command_list = command.split()
    action = command_list[0]
    if action == 'Loot':
        for i in range(1, len(command_list)):
            item = command_list[i]
            if item not in loot:
                loot.insert(0, item)
    elif action == 'Drop':
        position = int(command_list[1])
        if position <= len(loot):
            chest = loot[position]
            loot.pop(position)
            loot.append(chest)

    elif action == 'Steal':
        position = int(command_list[1])
        if position >= len(loot):
            print(', '.join(loot))
            loot.clear()
        else:
            stolen = loot[-position:]
            print(', '.join(stolen))
            loot = loot[:-position]

    command = input()
items = len(loot)
if not items:
    print("Failed treasure hunt.")
else:
    avg_gain = len(''.join(loot)) / items
    print(f'Average treasure gain: {avg_gain:.2f} pirate credits.')
