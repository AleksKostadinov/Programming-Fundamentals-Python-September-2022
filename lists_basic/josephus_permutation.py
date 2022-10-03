list_of_numbers = [int(number) for number in input().split()]
k_number = int(input())
executed_list = []
counter = 0
index = 0
while len(list_of_numbers) > 0:
    counter += 1

    if counter % k_number == 0:
        executed_list.append(list_of_numbers.pop(index))
    else:
        index += 1

    if index >= len(list_of_numbers):
        index = 0

print(str(executed_list).replace(' ', ''))