command = input()
dwarf_dict = {}
result_list = []
while command != 'Once upon a time':
    name, colour, score = command.split(' <:> ')
    score = int(score)
    if colour not in dwarf_dict:
        dwarf_dict[colour] = {name: score}
    else:
        if name not in dwarf_dict[colour]:
            dwarf_dict[colour].update({name: score})
        else:
            if dwarf_dict[colour][name] < score:
                dwarf_dict[colour][name] = score

    command = input()
for colour in dwarf_dict:
    for name, score in dwarf_dict[colour].items():
        result_list.append({'len': len(dwarf_dict[colour]), 'name': name, 'score': score, 'colour': colour})
for show in sorted(result_list, key=lambda x: (-x['score'], -x['len'])):
    print(f"({show['colour']}) {show['name']} <-> {show['score']}")
