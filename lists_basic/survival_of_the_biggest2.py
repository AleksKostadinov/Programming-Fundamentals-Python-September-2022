list_of_integers = input().split()
count_of_numbers_to_remove = int(input())

for integer in range(len(list_of_integers)):
    list_of_integers[integer] = int(list_of_integers[integer])

for removal in range(count_of_numbers_to_remove):
    list_of_integers.remove(min(list_of_integers))

print(', '.join(map(str, list_of_integers)))
