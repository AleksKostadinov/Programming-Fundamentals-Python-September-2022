list_of_integers = list(map(int, input().split()))
count_of_numbers_to_remove = int(input())

for removal in range(count_of_numbers_to_remove):
    list_of_integers.remove(min(list_of_integers))

print(', '.join(map(str, list_of_integers)))
