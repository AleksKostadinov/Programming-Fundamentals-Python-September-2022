first_list = input().split(', ')
second_list = input().split(', ')
string_in = []
for first in first_list:
    for second in second_list:
        if first in second:
            string_in.append(first)
            break
print(string_in)