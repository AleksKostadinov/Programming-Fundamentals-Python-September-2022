factor = int(input())
count = int(input())
my_list = []
multiplayer = factor
length = count * factor

for j in range(factor, length + 1, multiplayer):
    my_list.append(j)

print(my_list)