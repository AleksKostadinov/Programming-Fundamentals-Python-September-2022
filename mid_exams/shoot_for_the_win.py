targets = [int(x) for x in input().split()]
list_shot = []
counter = 0
while True:
    command = input()
    if command == 'End':
        break
    shot = int(command)
    if shot >= len(targets):
        continue
    else:
        index_shot = targets[shot]
        targets.pop(shot)
        targets.insert(shot, -1)
        list_shot.append(shot)
        counter += 1
        for index, value in enumerate(targets):
            if index in list_shot:
                continue
            elif value > index_shot:
                targets[index] -= index_shot
                # targets.pop(index)
                # targets.insert(index, value - index_shot)
            else:
                targets[index] += index_shot
                # targets.pop(index)
                # targets.insert(index, value + index_shot)
print(f"Shot targets: {counter} -> {' '.join(map(str,targets))}")