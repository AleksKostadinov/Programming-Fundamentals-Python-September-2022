dungeons_rooms = input().split('|')
health = 100
bitcoin = 0
best_room = 0
dead = False
for room in range(len(dungeons_rooms)):
    rooms = dungeons_rooms[room].split()
    command = rooms[0]
    number = int(rooms[1])

    if command == 'potion':
        if health + number >= 100:
            number = 100 - health
            health = 100
        else:
            health += number
        print(f"You healed for {number} hp.\nCurrent health: {health} hp.")

    elif command == 'chest':
        bitcoin += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            dead = True
            print(f"You died! Killed by {command}.")
    best_room += 1
    if dead:
        print(f"Best room: {best_room}")
        break
if health > 0:
    print(f"You've made it!\nBitcoins: {bitcoin}\nHealth: {health}")
