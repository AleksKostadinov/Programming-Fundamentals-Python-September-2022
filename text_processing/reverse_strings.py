command = input()

while command != 'end':
    reversed_command = [x for x in reversed(command)]
    print(f"{command} = {''.join(reversed_command)}")
    command = input()
    