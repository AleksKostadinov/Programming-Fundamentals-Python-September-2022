number = int(input())

for i in range(number):
    str_input = input()

    if ',' in str_input:
        print(f"{str_input} is not pure!")
    elif '.' in str_input:
        print(f"{str_input} is not pure!")
    elif '_' in str_input:
        print(f"{str_input} is not pure!")
    else:
        print(f"{str_input} is pure.")