number_list = list(map(int, input().split(', ')))
even_list = [int(i) for i, d in enumerate(number_list) if d % 2 == 0]
print(even_list)