number = int(input())
cars = {}

for car in range(number):
    make, kms, liters = input().split('|')
    if make not in cars:
        cars[make] = 0
    cars[make] = {'kms': int(kms), 'liters': int(liters)}

command = input()
while command != 'Stop':
    command_list = command.split(' : ')
    action = command_list[0]
    if action == 'Drive':
        car, distance, fuel = command_list[1], int(command_list[2]), int(command_list[3])
        if cars[car]['liters'] >= fuel:
            cars[car]['kms'] += distance
            cars[car]['liters'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print('Not enough fuel to make that ride')
        if cars[car]['kms'] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]
    elif action == 'Refuel':
        car, fuel = command_list[1], int(command_list[2])
        if (cars[car]['liters'] + fuel) <= 75:
            cars[car]['liters'] += fuel
            print(f"{car} refueled with {fuel} liters")
        else:
            refueled = 75 - cars[car]['liters']
            cars[car]['liters'] = 75
            print(f"{car} refueled with {refueled} liters")
    elif action == 'Revert':
        car, km = command_list[1], int(command_list[2])
        if (cars[car]['kms'] - km) >= 10000:
            cars[car]['kms'] -= km
            print(f"{car} mileage decreased by {km} kilometers")
        else:
            cars[car]['kms'] = 10000
    command = input()
for car, info in cars.items():
    print(f"{car} -> Mileage: {cars[car]['kms']} kms, Fuel in the tank: {cars[car]['liters']} lt.")
