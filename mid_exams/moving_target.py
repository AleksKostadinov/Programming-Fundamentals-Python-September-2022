targets = [int(x) for x in input().split()]

while True:
    command = input().split()
    if command[0] == 'End':
        break
    if command[0] == 'Shoot':
        # index if it exists or not
        index_shot = command[1]
        if command[1] <= len(targets):
            targets[index_shot] -= command[2]
            if targets[index_shot] == 0 or command[2] > targets[index_shot]: # if targets[index_shot] <= 0
                targets.remove(0)
        else:
            pass
    elif command[0] == 'Add':
        # index if it exists or not
        index_shot = command[1]
        if command[1] <= len(targets):
            targets.insert(index_shot, )
            # o	If not, print: "Invalid placement!"
        else:
            print(f"Invalid placement!")
    elif command[0] == 'Strike':
        index_shot = command[1]
        # Remove the target at the given index and the ones before and after it depending on the radius.
        # If any of the indices in the range is invalid, print: "Strike missed!" and skip this command.
        if command[1] <= len(targets):
            targets.pop(index_shot)
        else:
            pass
    