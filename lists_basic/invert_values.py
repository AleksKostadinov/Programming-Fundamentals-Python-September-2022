strings = input().split()
my_list = []

for i in strings:
    if int(i) <= 0:
        my_list.append(abs(int(i)))

    else:
        my_list.append(-abs(int(i)))

print(my_list)
