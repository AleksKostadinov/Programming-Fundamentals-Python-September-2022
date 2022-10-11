energy = int(input())
win_battle = 0

while True:
    command = input()
    if command == 'End of battle':
        print(f"Won battles: {win_battle}. Energy left: {energy}")
        break
    distance = int(command)

    if energy < distance:
        print(f"Not enough energy! Game ends with {win_battle} won battles and {energy} energy")
        break
    energy -= distance
    win_battle += 1
    if win_battle % 3 == 0:
        energy += win_battle