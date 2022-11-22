import re

destination = input()
command = input()
pattern = r'(\w+)'
while command != 'Travel':
    matches = re.findall(pattern, command)
    if matches[0] == 'Add':
        index = int(matches[2])
        string = matches[3]
        if 0 <= index < len(destination):
            destination = destination[:index] + string + destination[index:]
            print(destination)
        else:
            print(destination)
    elif matches[0] == 'Remove':
        start_index = int(matches[2])
        end_index = int(matches[3])
        if 0 <= start_index <= end_index < len(destination):
            destination = destination[:start_index] + destination[end_index + 1:]
            print(destination)
        else:
            print(destination)
    elif matches[0] == 'Switch':
        old_string = matches[1]
        new_string = matches[2]
        if old_string in destination:
            destination = destination.replace(old_string, new_string)
            print(destination)
        else:
            print(destination)
    command = input()
print(f'Ready for world tour! Planned stops: {destination}')
