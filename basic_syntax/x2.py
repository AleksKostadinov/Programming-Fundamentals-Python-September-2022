num = int(input())
i = 0
j = num - 1

for row in range(num):
    for col in range(num):
        if row == i and col == j:
            print('x', end='')
            i += 1
            j -= 1
        elif row == col:
            print('x', end='')
        else:
            print(end=' ')
    print()
