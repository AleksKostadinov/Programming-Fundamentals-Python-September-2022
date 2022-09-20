num = int(input())
total_sum = 0

counter = 0
for odd in range(1, 101):
    if odd % 2 != 0:
        counter += 1
        if counter > num:
            break
        print(odd)
        total_sum += odd
print(f'Sum: {total_sum}')