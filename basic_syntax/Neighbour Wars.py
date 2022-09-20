pesho_damage = int(input())
gosho_damage = int(input())

turn = 0
pesho_health = 100
gosho_health = 100
pesho_wins = False
gosho_wins = False
winner = ''
while True:
    turn += 1
    if turn % 2 != 0:
        gosho_health -= pesho_damage
        pesho_hit = 'Roundhouse kick'
        if gosho_health <= 0:
            pesho_wins = True
            winner = 'Pesho'
            break
        print(f"Pesho used {pesho_hit} and reduced Gosho to {gosho_health} health.")
    else:
        pesho_health -= gosho_damage
        gosho_hit = 'Thunderous fist'
        if pesho_health <= 0:
            gosho_wins = True
            winner = 'Gosho'
            break
        print(f"Gosho used {gosho_hit} and reduced Pesho to {pesho_health} health.")

    if turn % 3 == 0:
        gosho_health += 10
        pesho_health += 10

if pesho_wins:
    print(f"{winner} won in {turn}th round.")
elif gosho_wins:
    print(f"{winner} won in {turn}th round.")