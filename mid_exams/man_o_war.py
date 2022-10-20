def fire_func(commands):
    index = int(commands[1])
    damage = int(commands[2])
    global flag_end
    if 0 <= index < len(warship):
        warship[index] -= damage
        if warship[index] <= 0:
            print('You won! The enemy ship has sunken.')
            flag_end = True
            return flag_end


def defend_func(commands):
    start_index = int(commands[1])
    end_index = int(commands[2])
    damage = int(commands[3])
    global pirate_ship, flag_end
    if 0 <= start_index <= end_index <= len(pirate_ship) - 1:
        damaged_zone_list = pirate_ship[:start_index]
        for zone in pirate_ship[start_index:end_index + 1]:
            damaged_zone = zone - damage
            damaged_zone_list.append(damaged_zone)
            if damaged_zone <= 0:
                print(f"You lost! The pirate ship has sunken.")
                flag_end = True
                return flag_end
        damaged_zone_list += pirate_ship[end_index + 1:]
        pirate_ship = damaged_zone_list
        return pirate_ship


def repair_func(commands):
    index = int(commands[1])
    add_health = int(commands[2])
    if 0 <= index in range(len(pirate_ship)):
        pirate_ship[index] += add_health
        if pirate_ship[index] > max_health:
            pirate_ship[index] = max_health


def status_func():
    count = 0
    for zone in pirate_ship:
        if zone < (max_health * 0.2):
            count += 1
    print(f'{count} sections need repair.')


pirate_ship = list(map(int, input().split('>')))
warship = [int(x) for x in input().split('>')]
max_health = int(input())
command = input()
flag_end = False
while command != 'Retire':
    command_list = command.split()
    action = command_list[0]
    if action == 'Fire':
        fire_func(command_list)
    elif action == 'Defend':
        defend_func(command_list)
    elif action == 'Repair':
        repair_func(command_list)
    elif action == 'Status':
        status_func()
    if flag_end:
        break
    command = input()
if not flag_end:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")
