word = input()
my_list = []
for i, d in enumerate(word):
    if d.isupper():
        my_list += [i]
print(my_list, end='')
