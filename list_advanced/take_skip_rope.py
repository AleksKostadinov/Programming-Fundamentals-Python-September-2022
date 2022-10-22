encrypted_list = input()

int_list = [int(x) for x in encrypted_list if x.isdigit()]
string_list = [x for x in encrypted_list if not x.isdigit()]
take_list = [int(d) for i, d in enumerate(int_list) if i % 2 == 0]
skip_list = [int(d) for i, d in enumerate(int_list) if i % 2 != 0]

taken_string_list = []
for i in range(len(take_list)):
    taken_string_list += string_list[:take_list[i]]
    string_list = string_list[take_list[i]:]

    string_list = string_list[skip_list[i]:]

print(''.join(taken_string_list))
