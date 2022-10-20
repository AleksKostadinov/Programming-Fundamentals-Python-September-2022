neighborhood_list = list(map(int, input().split('@')))
command = input()
house_jump = 0
cupid_fails = 0
while command != 'Love!':
    command_list = command.split()
    index_jump = int(command_list[1])
    house_jump += index_jump
    command = input()

    if house_jump >= len(neighborhood_list):
        house_jump = 0
    if 0 <= house_jump < len(neighborhood_list):
        if neighborhood_list[house_jump] >= 2:
            neighborhood_list[house_jump] -= 2
            if neighborhood_list[house_jump] == 0:
                print(f'Place {house_jump} has Valentine\'s day.')
        elif neighborhood_list[house_jump] == 0:
            print(f'Place {house_jump} already had Valentine\'s day.')

for house in neighborhood_list:
    if house != 0:
        cupid_fails += 1

print(f'Cupid\'s last position was {house_jump}.')
if cupid_fails == 0:
    print(f'Mission was successful.')
else:
    print(f'Cupid has failed {cupid_fails} places.')
