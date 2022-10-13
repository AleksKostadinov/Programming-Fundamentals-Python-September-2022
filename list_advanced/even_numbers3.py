number_list = list(map(int, input().split(', ')))
even_list = [x for x in range(len(number_list)) if number_list[x] % 2 == 0]
print(even_list)