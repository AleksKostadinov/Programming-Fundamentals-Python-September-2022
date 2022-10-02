money_list = input().split(", ")
money_list_as_digit = []

for element in money_list:
    money_list_as_digit.append(int(element))
beggars = int(input())
starting_index = 0
final_list = []

while starting_index < beggars:
    sum_beggar = 0
    for current_index in range(starting_index, len(money_list_as_digit), beggars):
        sum_beggar += money_list_as_digit[current_index]
    final_list.append(sum_beggar)
    starting_index += 1

print(final_list)