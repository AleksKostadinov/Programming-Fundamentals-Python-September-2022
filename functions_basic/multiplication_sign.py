def multiplication_sign(fst, snd, trd):
    numbers_list = [fst, snd, trd]
    is_negative = [num for num in numbers_list if num < 0]
    if 0 in numbers_list:
        return 'zero'
    elif len(is_negative) % 2 == 0:
        return 'positive'
    else:
        return 'negative'


first = int(input())
second = int(input())
third = int(input())
print(multiplication_sign(first, second, third))
