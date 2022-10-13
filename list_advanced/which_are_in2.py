first_list = input().split(', ')
second_list = input()

string_in = [ele for ele in first_list if ele in second_list]
print(string_in)