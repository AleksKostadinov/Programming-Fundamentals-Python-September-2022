def perfect_or_not(num):
    sums = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            sums += divisor
    if num == sums:
        return 'We have a perfect number!'
    return "It's not so perfect."


number = int(input())
print(perfect_or_not(number))
