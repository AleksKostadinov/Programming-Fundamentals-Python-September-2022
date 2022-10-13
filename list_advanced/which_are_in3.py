def which_are_in(first, second):
    for f in first:
        for s in second:
            if f in s:
                string_in.append(f)
                break
    return string_in


first_list = input().split(', ')
second_list = input().split(', ')
string_in = []

print(which_are_in(first_list, second_list))