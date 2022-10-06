list_of_numbers = [float(num) for num in input().split()]


def rounding_func(number):
    result = [round(num) for num in number]
    return result


print(rounding_func(list_of_numbers))
