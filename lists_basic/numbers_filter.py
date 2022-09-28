lines = int(input())
positive_list = []
negative_list = []
even_list = []
odd_list = []
for line in range(lines):
    integer = int(input())

    if integer % 2 == 0:
        even_list.append(integer)
    elif integer % 2 != 0:
        odd_list.append(integer)
    if integer >= 0:
        positive_list.append(integer)
    else:
        negative_list.append(integer)

command = input()
if command == 'even':
    print(even_list)
elif command == 'odd':
    print(odd_list)
elif command == 'positive':
    print(positive_list)
else:
    print(negative_list)