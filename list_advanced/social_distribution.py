population = list(map(int, input().split(', ')))
minimum_wealth = int(input())
max_number = 0
for number, value in enumerate(population):
    max_number = max(population)
    max_number_index = population.index(max_number)
    if value < minimum_wealth <= max_number:
        population[number] = minimum_wealth
        population[max_number_index] = max_number - (minimum_wealth - value)
if min(population) < minimum_wealth:
    print(f'No equal distribution possible')
else:
    print(population)
