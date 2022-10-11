def average_number_list(list_nums):
    avg_list = []
    avg_number = sum(list_nums) / len(list_nums)
    for num in reversed(sorted(list_numbers)):
        if num > avg_number:
            avg_list.append(num)
    return avg_list[:5]


list_numbers = [int(x) for x in input().split()]

if not average_number_list(list_numbers):
    print('No')
else:
    print(' '.join(map(str, average_number_list(list_numbers))))
