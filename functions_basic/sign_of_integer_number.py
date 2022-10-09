def sign_number(num):
    if num == 0:
        return f'The number {num} is zero.'
    elif num > 0:
        return f'The number {num} is positive.'
    else:
        return f'The number {num} is negative.'


number = int(input())
print(sign_number(number))
