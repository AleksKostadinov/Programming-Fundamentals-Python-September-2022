number_rooms = int(input())
free_chairs = 0
needed_chairs = 0
for room in range(1, number_rooms + 1):
    chairs, visitors = input().split()
    diff = len(chairs) - int(visitors)
    if diff >= 0:
        free_chairs += diff
    else:
        needed_chairs += abs(diff)
        print(f"{abs(diff)} more chairs needed in room {room}")

if free_chairs >= needed_chairs:
    print(f"Game On, {free_chairs} free chairs left")

