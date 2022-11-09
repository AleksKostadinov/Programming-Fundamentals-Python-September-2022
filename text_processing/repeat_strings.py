string_list = input().split()

for word in string_list:
    print(f"{''.join(word * len(word))}", end='')
    