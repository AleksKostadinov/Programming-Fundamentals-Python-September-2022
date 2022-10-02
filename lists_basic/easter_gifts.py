gifts = input().split()
command = input()
while command != 'No Money':
    command = command.split()
    if command[0] == 'OutOfStock':
        for word in range(len(gifts)):
            if gifts[word] == command[1]:
                gifts[word] = 'None'
    elif command[0] == 'Required':
        for word in range(len(gifts)):
            if word == int(command[2]):
                gifts[word] = command[1]
    elif command[0] == 'JustInCase':
        gifts[-1] = command[1]
    command = input()

while 'None' in gifts:
    gifts.remove('None')

print(' '.join(gifts))
