lines = input()
for index, line in enumerate(lines):
    if ':' == line:
        print(f':{lines[index+1]}')
