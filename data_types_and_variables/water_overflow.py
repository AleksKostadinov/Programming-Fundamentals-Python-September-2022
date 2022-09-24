lines = int(input())
capacity = 255
total = 0
for line in range(lines):
    liters = int(input())

    capacity -= liters
    total += liters
    if capacity < 0:
        capacity += liters
        total -= liters
        print('Insufficient capacity!')
        continue

print(total)