number = int(input())

for i in range(1, number + 1):
    first_digit = i // 10
    second_digit = i % 10

    if first_digit + second_digit == 5 or first_digit + second_digit == 7 or first_digit + second_digit == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
