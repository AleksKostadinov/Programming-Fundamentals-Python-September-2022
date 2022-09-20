name = input()
current_health = int(input())
maximum_health = int(input())
current_energy = int(input())
maximum_energy = int(input())

left_health = maximum_health - current_health
left_energy = maximum_energy - current_energy

str_health = current_health * '|' + left_health * '.'
str_energy = current_energy * '|' + left_energy * '.'

print(f'Name: {name}')
print(f'Health: |{str_health}|')
print(f'Energy: |{str_energy}|')
