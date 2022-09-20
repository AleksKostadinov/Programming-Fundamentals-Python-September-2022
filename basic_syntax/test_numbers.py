n = int(input())
m = int(input())
boundary = int(input())
total_number = 0
count = 0

for i in range(n, 0, - 1):
    for j in range(1, m + 1):
        if total_number >= boundary:
            break
        total_number += (i * j) * 3
        count += 1

if total_number < boundary:
    print(f'{count} combinations')
    print(f"Sum: {total_number}")
else:
    print(f'{count} combinations')
    print(f'Sum: {total_number} >= {boundary}')

