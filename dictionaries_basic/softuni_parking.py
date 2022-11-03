def register_func(names, plates, register_dicts):
    if names in register_dicts:
        return f"ERROR: already registered with plate number {plates}"
    register_dicts[names] = plates
    return f'{names} registered {plates} successfully'


def unregister_func(names, register_dicts):
    if names in register_dicts:
        register_dicts.pop(names)
        return f'{names} unregistered successfully'
    return f'ERROR: user {names} not found'


number_commands = int(input())
register_dict = {}
for num in range(number_commands):
    command = input().split()
    name = command[1]
    if len(command) > 2:
        plate = command[2]
        print(register_func(name, plate, register_dict))
    else:
        print(unregister_func(name, register_dict))
for key, value in register_dict.items():
    print(f"{key} => {value}")
