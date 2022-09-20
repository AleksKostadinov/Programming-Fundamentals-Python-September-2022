budget = int(input())
command = input()
is_bought = True
while command != 'End':
    bought = int(command)
    budget -= bought
    if budget < 0:
        is_bought = False
        break
    command = input()

if is_bought:
    print(f'You bought everything needed.')
else:
    print(f'You went in overdraft!')
