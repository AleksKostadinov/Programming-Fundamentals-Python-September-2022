word = input()

while word != 'End':
    for char in word:
        if word == 'SoftUni':
            continue
        else:
            print(char * 2, end='')
    if word != 'SoftUni':
        print()
    word = input()
