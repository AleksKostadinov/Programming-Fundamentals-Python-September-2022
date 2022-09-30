cards = input().split()
shuffle = int(input())

length = len(cards)
mid = int(length / 2)

for i in range(0, shuffle):
    my_list = []
    for p in range(0, mid):
        my_list.append(cards[p])
        my_list.append(cards[mid])
        mid += 1
    cards = my_list
    mid = int(length / 2)

print(my_list)
