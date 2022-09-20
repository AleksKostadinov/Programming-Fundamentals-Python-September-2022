quantity = int(input())
days_left = int(input())
spirit = 0
pr_ornament_set = 2
pr_tree_skirt = 5
pr_tree_garland = 3
pr_tree_lights = 15
budget = 0
for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        budget += quantity * pr_ornament_set
        spirit += 5
    if day % 3 == 0:
        budget += quantity * (pr_tree_skirt + pr_tree_garland)
        spirit += 13
    if day % 5 == 0:
        budget += quantity * pr_tree_lights
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        budget += pr_tree_skirt + pr_tree_garland + pr_tree_lights
if days_left % 10 == 0:
    spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {spirit}")
