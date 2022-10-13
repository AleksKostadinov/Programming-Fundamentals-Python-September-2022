number_list = list(map(int, input().split(', ')))
even_list = []
for i, d in enumerate(number_list):
    if d % 2 == 0:
        even_list.append(i)
print(even_list)