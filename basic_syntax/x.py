num = int(input())

for row in range(num):
    for col in range(num):
        if row == col or col == num - 1 - row:
            print('x', end='')
        else:
            print(' ', end='')
    print()
