def calc_inventory(input_lines: list, elements_dict: dict):
    for i in range(0, len(input_lines), 2):
        quantity = int(input_lines[i])
        material = input_lines[i + 1].lower()
        elements_dict[material] = elements_dict.get(material, 0)
        elements_dict[material] += quantity
        if elements_dict["shards"] >= 250 or elements_dict["fragments"] >= 250 or elements_dict["motes"] >= 250:
            return True


def legendary_item(needed_items: list, gained_items: dict):
    for item in needed_items:
        if gained_items[item] >= 250:
            gained_items[item] -= 250
            if item == "shards":
                return "Shadowmourne obtained!"
            elif item == "fragments":
                return "Valanyr obtained!"
            elif item == "motes":
                return "Dragonwrath obtained!"


key_materials = ["shards", "fragments", "motes"]
elements = dict.fromkeys(key_materials, 0)
reached_goal = False
while not reached_goal:
    line = input().lower().split()
    reached_goal = calc_inventory(line, elements)

print(legendary_item(key_materials, elements))
[print(f"{key}: {value}") for key, value in elements.items()]
