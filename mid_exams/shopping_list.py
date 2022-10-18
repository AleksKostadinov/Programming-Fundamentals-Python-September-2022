def urgent_func(groceries):
    if item not in groceries:
        groceries.insert(0, item)


def unnecessary_func(groceries):
    if item in groceries:
        groceries.remove(item)


def correct_func(groceries):
    if old_item in groceries:
        old_item_index = groceries.index(old_item)
        groceries[old_item_index] = new_item


def rearrange_func(groceries):
    if item in groceries:
        groceries.remove(item)
        groceries.append(item)


groceries_list = input().split('!')
command = input()
while command != 'Go Shopping!':
    command_list = command.split()
    action = command_list[0]
    item = command_list[1]
    if action == 'Urgent':
        urgent_func(groceries_list)
    elif action == 'Unnecessary':
        unnecessary_func(groceries_list)
    elif action == 'Correct':
        old_item = command_list[1]
        new_item = command_list[2]
        correct_func(groceries_list)
    elif action == 'Rearrange':
        rearrange_func(groceries_list)
    command = input()
print(', '.join(groceries_list))