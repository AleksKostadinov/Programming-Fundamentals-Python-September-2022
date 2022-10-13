targets = list(map(int, input().split()))

while True:
    length = len(targets)
    command = input().split()
    if command[0] == 'End':
        break
    index_shot = int(command[1])
    power_shot = int(command[2])
    if command[0] == 'Shoot':
        if index_shot in range(length):
            if targets[index_shot] > power_shot:
                targets[index_shot] -= power_shot
            else:
                targets.pop(index_shot)
    elif command[0] == 'Add':
        if index_shot in range(length):
            targets.insert(index_shot, power_shot)
        else:
            print(f"Invalid placement!")
    elif command[0] == 'Strike':
        if index_shot >= power_shot and (index_shot + power_shot) < length:
            del targets[index_shot - power_shot:index_shot + power_shot + 1]
        else:
            print(f"Strike missed!")
print(*targets, sep="|")