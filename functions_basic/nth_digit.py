def find_nth_digit(numbers, index):
    for i, d in enumerate(reversed(numbers)):
        if i == index - 1:
            return d


some_numbers = input()
n_index = int(input())
print(find_nth_digit(some_numbers, n_index))
