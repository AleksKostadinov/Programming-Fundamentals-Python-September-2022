to_do_list = [0] * 10
while True:
    command = input()
    if command == 'End':
        break
    notes = command.split('-')
    priority = int(notes[0]) - 1
    note = notes[1]
    to_do_list.pop(priority)
    to_do_list.insert(priority, note)
result = [element for element in to_do_list if element != 0]
print(result)
    