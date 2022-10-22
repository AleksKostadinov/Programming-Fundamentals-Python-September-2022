def attack(attack_lists, attack_row, attack_col):
    global destroyed_ships
    destroyed = False
    if attack_lists[attack_row][attack_col] > 0:
        attack_lists[attack_row][attack_col] -= 1
        if attack_lists[attack_row][attack_col] == 0:
            destroyed = True
            destroyed_ships += 1
    return destroyed


rows = int(input())
lists = []
destroyed_ships = 0
for row in range(rows):
    line = list(map(int, input().split()))
    lists.append(line)

squares = input().split()

for square in squares:
    row_attack, col_attack = list(map(int, square.split('-')))
    attack(lists, row_attack, col_attack)
print(destroyed_ships)