char_list = input().split(', ')
char_dict = {}

for char in char_list:
    char_dict[char] = ord(char)
print(char_dict)
