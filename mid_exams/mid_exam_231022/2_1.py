def blacklist_func(friends_lists):
    if name in friends_lists:
        index_name = friends_lists.index(name)
        blacklisted.append(name)
        friends_lists.remove(name)
        friends_lists.insert(index_name, 'Blacklisted')
        print(f"{name} was blacklisted.")
    else:
        print(f'{name} was not found.')
    return friends_lists


def error_func(friends_lists):
    global lost_name
    if 0 <= error_index < len(friends_lists):
        name_error = friends_lists[error_index]
        if name_error not in blacklisted and name_error != 'Lost' and name_error != 'Blacklisted':
            friends_lists[error_index] = 'Lost'
            lost_name += 1
            print(f"{name_error} was lost due to an error.")
    return friends_lists


def change_func(friends_lists):
    index = int(command_list[1])

    if 0 <= index < len(friends_lists):
        new_name = command_list[2]
        old_name = friends_lists[index]
        friends_lists[index] = new_name
        print(f"{old_name} changed his username to {new_name}.")
    return friends_lists


friends_list = input().split(', ')
command = input()
blacklisted = []
lost_name = 0
while command != 'Report':
    command_list = command.split()
    action = command_list[0]
    if action == 'Blacklist':
        name = command_list[1]
        friends_list = blacklist_func(friends_list)
    elif action == 'Error':
        error_index = int(command_list[1])
        friends_list = error_func(friends_list)
    elif action == 'Change':
        friends_list = change_func(friends_list)
    command = input()
number_blacklisted = len(blacklisted)
print(f"Blacklisted names: {number_blacklisted}")
print(f"Lost names: {lost_name}")
print(' '.join(friends_list))
