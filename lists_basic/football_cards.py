red_cards = input().split()
banned_teamA = []
banned_teamB = []
red_teamA = 11
red_teamB = 11
is_terminated = False
while not is_terminated:
    if 'A' in red_cards[0]:
        if red_cards[0] in banned_teamA:
            red_cards.pop(0)
            continue
        banned_teamA.append(red_cards[0])
        red_cards.pop(0)
        red_teamA -= 1

    elif 'B' in red_cards[0]:
        if red_cards[0] in banned_teamB:
            red_cards.pop(0)
            continue
        banned_teamB.append(red_cards[0])
        red_cards.pop(0)
        red_teamB -= 1

    if red_teamA < 7 or red_teamB < 7:
        is_terminated = True
        break
    if not red_cards:
        break

print(f'Team A - {red_teamA}; Team B - {red_teamB}')

if is_terminated:
    print("Game was terminated")
