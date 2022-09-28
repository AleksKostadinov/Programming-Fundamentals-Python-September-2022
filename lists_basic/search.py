lines = int(input())
special_word = input()
my_list = []
special_list = []
for line in range(lines):
    text = input()
    my_list.append(text)

    if special_word in text:
        special_list.append(text)

print(my_list)
print(special_list)
