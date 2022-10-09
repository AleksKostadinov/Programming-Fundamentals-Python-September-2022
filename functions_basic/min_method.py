def get_min_from_three(fst, snd):
    a = min(fst, snd)
    return a


def get_min(a, b):
    return min(a, b)


first_number = int(input())
second_number = int(input())
third_number = int(input())
sum_first_two = get_min_from_three(first_number, second_number)

print(get_min(sum_first_two, third_number))
