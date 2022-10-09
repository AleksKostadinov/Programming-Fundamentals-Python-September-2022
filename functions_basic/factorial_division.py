def factorial_division(fst, snd):
    sum_fst = 1
    sum_snd = 1
    for first in range(1, fst + 1):
        sum_fst *= first
    for second in range(1, snd + 1):
        sum_snd *= second
    result = sum_fst / sum_snd
    return f'{result:.2f}'


first_number = int(input())
second_number = int(input())
print(factorial_division(first_number, second_number))
