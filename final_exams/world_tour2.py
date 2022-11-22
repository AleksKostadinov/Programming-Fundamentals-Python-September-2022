import re


def add_stop(destinations):
    index = int(matches[2])
    string = matches[3]
    if 0 <= index < len(destinations):
        destinations = destinations[:index] + string + destinations[index:]
    return destinations


def remove_stop(destinations):
    start_index = int(matches[2])
    end_index = int(matches[3])
    if 0 <= start_index <= end_index < len(destinations):
        destinations = destinations[:start_index] + destinations[end_index + 1:]
    return destinations


def switch(destinations):
    old_string = matches[1]
    new_string = matches[2]
    if old_string in destinations:
        destinations = destinations.replace(old_string, new_string)
    return destinations


destination = input()
command = input()
pattern = r'(\w+)'
while command != 'Travel':
    matches = re.findall(pattern, command)
    if matches[0] == 'Add':
        destination = add_stop(destination)
    elif matches[0] == 'Remove':
        destination = remove_stop(destination)
    elif matches[0] == 'Switch':
        destination = switch(destination)
    print(destination)
    command = input()
print(f'Ready for world tour! Planned stops: {destination}')
