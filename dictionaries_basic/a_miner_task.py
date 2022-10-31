sequence = input()
resource_dict = {}

while sequence != 'stop':
    resource = int(input())
    if sequence not in resource_dict:
        resource_dict[sequence] = 0
    resource_dict[sequence] += resource
    sequence = input()
for key, value in resource_dict.items():
    print(f'{key} -> {value}')
