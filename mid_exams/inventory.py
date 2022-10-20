def collect_func():
    if item not in collecting_items:
        collecting_items.append(item)


def drop_func():
    if item in collecting_items:
        collecting_items.remove(item)


def combine_func():
    if old_item in collecting_items:
        index_old = collecting_items.index(old_item)
        collecting_items.insert(index_old+1, new_item)


def renew_func():
    if item in collecting_items:
        collecting_items.remove(item)
        collecting_items.append(item)


collecting_items = input().split(', ')
command = input()

while command != 'Craft!':
    command_list = command.split(' - ')
    action = command_list[0]
    item = command_list[1]
    if action == 'Collect':
        collect_func()
    elif action == 'Drop':
        drop_func()
    elif action == 'Combine Items':
        old_item, new_item = item.split(':')
        combine_func()
    elif action == 'Renew':
        renew_func()

    command = input()
print(', '.join(collecting_items))