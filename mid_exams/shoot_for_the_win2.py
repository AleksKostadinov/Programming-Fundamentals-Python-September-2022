targets = list(map(int, input().split()))
counter = 0
shot = input()

while shot != "End":
    shot = int(shot)
    if shot < len(targets):
        if targets[shot] != -1:
            current_target = targets[shot]
            targets[shot] = -1
            counter += 1
            for target_index in range(len(targets)):
                if targets[target_index] != -1:
                    if targets[target_index] > current_target:
                        targets[target_index] -= current_target
                    else:
                        targets[target_index] += current_target

    shot = input()

result = " ".join(map(str, targets))
print(f"Shot targets: {counter} -> {result}")