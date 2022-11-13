secret_key = list(map(int, input().split()))
starting_key = secret_key.copy()
command = input()
while command != 'find':
    result = []
    for index, value in enumerate(command):
        if index < len(secret_key):
            key_index = index
        else:
            key_index = index % len(secret_key)
        result.append(chr(ord(value) - int(secret_key[key_index])))

    command = input()
    treasure_lst = ''.join(result).split('&')
    treasure = treasure_lst[1]
    coordinates_lst = ''.join(result).split('<')
    coordinates = coordinates_lst[1].replace('>', '')
    print(f'Found {treasure} at {coordinates}')
