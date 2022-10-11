def top_5(nums):
    avg = sum(nums) / len(nums)

    list_nums = [x for x in sorted(nums, reverse=True) if x > avg]

    if len(list_nums) != 0:
        return ' '.join(map(str, list_nums[:5]))
    else:
        return 'No'


numbers = list(map(int, input().split()))
print(top_5(numbers))