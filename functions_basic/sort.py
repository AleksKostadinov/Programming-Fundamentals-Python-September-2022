def sort_func(numbers):
    return sorted(numbers)


list_of_numbers = [int(x) for x in input().split()]
print(sort_func(list_of_numbers))
