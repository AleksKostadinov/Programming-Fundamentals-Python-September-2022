n = int(input())
greeting = ''
for i in range(n):
    number_message = int(input())

    if number_message == 88:
        greeting = 'Hello'
    elif number_message == 86:
        greeting = 'How are you?'
    elif number_message < 88:
        greeting = 'GREAT!'
    else:
        greeting = 'Bye.'
    print(f'{greeting}')