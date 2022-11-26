def create_heroes(number_of_heroes_):
    for _ in range(number_of_heroes_):
        hero, hp, mana = (int(x) if x.isdigit() else x for x in input().split())
        if hero not in heroes_dict:
            heroes_dict[hero] = {'hp': 0, 'mana': 0}
        heroes_dict[hero] = {'hp': hp, 'mana': mana}


def cast_spell(other_):
    hero, mana_needed, spell_name = other_
    if heroes_dict[hero]['mana'] >= mana_needed:
        heroes_dict[hero]['mana'] -= mana_needed
        return f"{hero} has successfully cast {spell_name} and now has {heroes_dict[hero]['mana']} MP!"
    return f"{hero} does not have enough MP to cast {spell_name}!"


def take_damage(other_):
    hero, damage, attacker = other_
    if heroes_dict[hero]['hp'] - damage > 0:
        heroes_dict[hero]['hp'] -= damage
        return f"{hero} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero]['hp']} HP left!"
    del heroes_dict[hero]
    return f"{hero} has been killed by {attacker}!"


def recharge(other_):
    hero, recharged_mana = other_
    if heroes_dict[hero]['mana'] + recharged_mana < 200:
        heroes_dict[hero]['mana'] += recharged_mana
        return f"{hero} recharged for {recharged_mana} MP!"
    amount_recovered = 200 - heroes_dict[hero]['mana']
    heroes_dict[hero]['mana'] = 200
    return f"{hero} recharged for {amount_recovered} MP!"


def heal(other_):
    hero, healed = other_
    if heroes_dict[hero]['hp'] + healed < 100:
        heroes_dict[hero]['hp'] += healed
        return f"{hero} healed for {healed} HP!"
    healed = 100 - heroes_dict[hero]['hp']
    heroes_dict[hero]['hp'] = 100
    return f"{hero} healed for {healed} HP!"


number_of_heroes = int(input())
heroes_dict = {}
create_heroes(number_of_heroes)
command = input()
while command != 'End':
    action, *other = (int(x) if x.isdigit() else x for x in command.split(' - '))
    if action == 'CastSpell':
        print(cast_spell(other))
    elif action == 'TakeDamage':
        print(take_damage(other))
    elif action == 'Recharge':
        print(recharge(other))
    elif action == 'Heal':
        print(heal(other))
    command = input()

for hero_name, info in heroes_dict.items():
    print(f"{hero_name}\n  HP: {heroes_dict[hero_name]['hp']}\n  MP: {heroes_dict[hero_name]['mana']}")
