sequence = input()
resource_dict = {}

while sequence != 'stop':
    resource = int(input())
    resource_dict[sequence] = resource_dict.get(sequence, 0)
    resource_dict[sequence] += resource
    sequence = input()
for key, value in resource_dict.items():
    print(f'{key} -> {value}')
