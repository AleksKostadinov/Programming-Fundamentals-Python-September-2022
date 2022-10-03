string_list = input().split(", ")

int_list = []
for i in string_list:
    if i == '0':
        string_list.remove('0')
        string_list.append(i)
print(list(map(int, string_list)))