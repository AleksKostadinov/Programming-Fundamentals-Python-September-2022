def data_type(first, second):
    if first == 'int':
        result = int(second) * 2
        return f'{result}'
    elif first == 'real':
        result = float(second) * 1.5
        return f'{result:.2f}'
    elif first == 'string':
        result = second
        return f'${result}$'


first_line = input()
second_line = input()
print(data_type(first_line, second_line))
