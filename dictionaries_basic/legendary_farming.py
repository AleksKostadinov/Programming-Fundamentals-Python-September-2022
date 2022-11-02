line = input().split()
result = {
    'Shadowmourne': 'shards',
    'Valanyr': 'fragments',
    'Dragonwrath': 'motes'
}
elements = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
reached_goal = False
while not reached_goal:
    for i in range(0, len(line), 2):
        quantity = int(line[i])
        material = line[i + 1].lower()
        elements[material] = elements.get(material, 0)
        elements[material] += quantity
        if elements["shards"] >= 250 or elements["fragments"] >= 250 or elements["motes"] >= 250:
            elements[material] -= 250
            for k, v in result.items():
                if v == material:
                    print(f'{k} obtained!')
                    reached_goal = True
                    break
            if reached_goal:
                break
    if reached_goal:
        break
    line = input().split()
if 'shards' in elements:
    print(f"shards: {elements['shards']}")
if 'fragments' in elements:
    print(f"fragments: {elements['fragments']}")
if 'motes' in elements:
    print(f"motes: {elements['motes']}")
for k, v in elements.items():
    if k == 'shards' or k == 'fragments' or k == 'motes':
        continue
    print(f'{k}: {v}')
