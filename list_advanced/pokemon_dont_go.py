def remove_number(numbers_list, index_number, removed):
    numbers_list.pop(index_number)
    for i in range(len(numbers_list)):
        if numbers_list[i] <= removed:
            numbers_list[i] += removed
        else:
            numbers_list[i] -= removed


numbers = input()
numbers = list(map(int, numbers.split()))
sum_removed_elements = 0

while len(numbers) > 0:
    index = int(input())
    if index < 0:
        index = 0
        removed_number = numbers[0]
        remove_number(numbers, index, removed_number)
        numbers.insert(0, numbers[-1])

    elif index >= len(numbers):
        index = - 1
        removed_number = numbers[-1]
        remove_number(numbers, index, removed_number)
        numbers.append(numbers[0])

    else:
        removed_number = numbers[index]
        remove_number(numbers, index, removed_number)

    sum_removed_elements += removed_number
print(sum_removed_elements)
