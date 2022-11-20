import re

health_pattern = r'[^\d\+\-\*\/\.]'
operator_pattern = r'[*\/]'
damage_pattern = r'([-+]?\d+(\.\d+)?)'
demon_book = {}
demons = input().split(',')
demons = [demon.strip() for demon in demons]

for demon in sorted(demons):
    health = re.findall(health_pattern, demon)
    health = sum(ord(x) for x in health)
    damage = re.findall(damage_pattern, demon)
    if damage:
        damage = sum(float(number[0]) for number in damage)
        operators = re.findall(operator_pattern, demon)
        if operators:
            for operator in operators:
                if operator == '*':
                    damage *= 2
                elif operator == '/':
                    damage /= 2
    else:
        damage = 0
    print(f'{demon} - {health} health, {damage:.2f} damage ')
