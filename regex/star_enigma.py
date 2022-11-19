import re

number_messages = int(input())
pattern = r'@([A-Za-z]+)[^\@|\-|\!|\:|\>]*:(\d+)[^\@|\-|\!|\:|\>]*!([A|D])![^\@|\-|\:|\>]*\->([\d])+[^\@|\!|\:|]*'
star_letters = r'[star]'

attacked_planets = []
destroyed_planets = []

for i in range(number_messages):
    messages = input()
    key = re.findall(star_letters, messages, flags=re.I)
    decrypted_message = ''.join([chr(ord(x) - len(key)) for x in messages])
    valid_message = re.search(pattern, decrypted_message)
    if valid_message:
        planet_name, population, attack_type, soldiers = valid_message.groups()
        if attack_type == 'A':
            attacked_planets.append(planet_name)
        elif attack_type == 'D':
            destroyed_planets.append(planet_name)
print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")
