friends_list = input().split(', ')
command = input()
blacklisted = []
lost_name = 0
while command != 'Report':
    command_list = command.split()
    action = command_list[0]
    if action == 'Blacklist':
        name = command_list[1]
        if name in friends_list:
            index_name = friends_list.index(name)
            blacklisted.append(name)
            friends_list.remove(name)
            friends_list.insert(index_name, 'Blacklisted')
            print(f"{name} was blacklisted.")
        else:
            print(f'{name} was not found.')
    elif action == 'Error':
        index = int(command_list[1])
        if 0 <= index < len(friends_list):
            name = friends_list[index]
            if name not in blacklisted and name != 'Lost' and name != 'Blacklisted':
                friends_list[index] = 'Lost'
                lost_name += 1
                print(f"{name} was lost due to an error.")
    elif action == 'Change':
        index = int(command_list[1])
        new_name = command_list[2]
        if 0 <= index < len(friends_list):
            old_name = friends_list[index]
            friends_list[index] = new_name
            print(f"{old_name} changed his username to {new_name}.")
    command = input()
number_blacklisted = len(blacklisted)
print(f"Blacklisted names: {number_blacklisted}")
print(f"Lost names: {lost_name}")
print(' '.join(friends_list))
