list_of_names = input().split(', ')

result = sorted(list_of_names, key=lambda x: (-len(x), x))
print(result)