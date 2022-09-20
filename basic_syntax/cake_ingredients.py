command = input()
count = 0
while command != 'Bake!':
    count += 1
    print(f'Adding ingredient {command}.')

    command = input()

print(f'Preparing cake with {count} ingredients.')