def even_func(numbers):
    even = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
    return even


list_of_numbers = [int(x) for x in input().split()]
print(even_func(list_of_numbers))
