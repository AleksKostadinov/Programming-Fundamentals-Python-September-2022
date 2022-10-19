def potion_func(number: int, hp):
    if hp + number < 100:
        hp += number
    else:
        hp = 100
        number = 100 - health
    print(f"You healed for {number} hp.")
    print(f"Current health: {hp} hp.")
    return hp


def chest_func(number: int):
    print(f"You found {number} bitcoins.")
    return number


def monster_func(number: int, monsters, hp):
    hp -= number
    if hp > 0:
        print(f"You slayed {monsters}.")
    else:
        print(f"You died! Killed by {monsters}.")
    return hp


rooms = input().split('|')
best_room = 0
health = 100
bitcoin = 0
win = True
for room in range(len(rooms)):
    command, amount = rooms[room].split()
    amount = int(amount)
    best_room = room + 1
    if command == 'potion':
        health = potion_func(amount, health)
    elif command == 'chest':
        bitcoin += chest_func(amount)
    else:
        health = monster_func(amount, command, health)
        if health <= 0:
            win = False
    if not win:
        print(f"Best room: {best_room}")
        break

if win:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")
