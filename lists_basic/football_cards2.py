red_cards = set(input().split())
red_teamA = 11
red_teamB = 11
is_terminated = False

for red_card in red_cards:
    if 'A' in red_card:
        red_teamA -= 1
    elif 'B' in red_card:
        red_teamB -= 1

    if red_teamA < 7 or red_teamB < 7:
        is_terminated = True
        break

print(f'Team A - {red_teamA}; Team B - {red_teamB}')

if is_terminated:
    print("Game was terminated")
