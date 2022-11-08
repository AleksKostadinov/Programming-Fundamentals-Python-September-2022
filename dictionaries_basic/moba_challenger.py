command = input()
result, players = {}, {}
while command != 'Season end':
    if 'vs' in command:
        player1, player2 = command.split(' vs ')
        if player1 in result and player2 in result:
            for positions in result[player1].keys():
                if positions in result[player2].keys():
                    if sum(result[player1].values()) > sum(result[player2].values()):
                        del result[player2]
                        break
                    else:
                        del result[player1]
                        break
    else:
        player, position, skill = command.split(' -> ')
        result[player] = result.get(player, {})
        result[player][position] = result[player].get(position, 0)
        if result[player][position] < int(skill):
            result[player][position] = int(skill)
    command = input()
for name in result.keys():
    players[name] = sum(result[name].values())
for name, skills in sorted(players.items(), key=lambda x: (-x[1], x[0])):
    print(f'{name}: {skills} skill')
    for position, skill in sorted(result[name].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")
