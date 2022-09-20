budget = float(input())
command = input()

total_costs = 0
not_found = False
is_game_time = True
while command != 'Game Time':

    if command == 'OutFall 4':
        price = 39.99
    elif command == 'CS: OG':
        price = 15.99
    elif command == 'Zplinter Zell':
        price = 19.99
    elif command == 'Honored 2':
        price = 59.99
    elif command == 'RoverWatch':
        price = 29.99
    elif command == 'RoverWatch Origins Edition':
        price = 39.99
    else:
        price = 0
        not_found = True

    budget -= price

    if budget < 0:
        budget += price
        price = 0
        print('Too Expensive')
    elif not_found:
        print('Not Found')
        not_found = False
    else:
        print(f'Bought {command}')

    total_costs += price

    if budget == 0:
        is_game_time = False
        break

    command = input()

    if command == 'Game Time':
        is_game_time = True
        break
if is_game_time:
    print(f'Total spent: ${total_costs:.2f}. Remaining: ${budget:.2f}')
else:
    print('Out of money!')