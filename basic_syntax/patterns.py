number = int(input())

for row in range(number):
    for col in range(row):
        print('*', end='')
    print('*')

for row in range(number - 1, 0, -1):
    for col in range(row - 1):
        print('*', end='')
    print('*')
