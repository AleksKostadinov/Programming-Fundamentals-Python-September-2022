def even_odd(num):
    sum_even, sum_odd = 0, 0
    for digit in num:
        digit = int(digit)
        if digit % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


number = input()
print(even_odd(number))
