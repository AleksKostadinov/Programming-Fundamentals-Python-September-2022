budget = float(input())
pr_kg_flour = float(input())
pr_pk_eggs = pr_kg_flour * 0.75
pr_quarter_milk = (pr_kg_flour * 1.25) / 4
pr_loaf = pr_pk_eggs + pr_kg_flour + pr_quarter_milk
number_of_loaves = 0
colored_eggs = 0

while budget > pr_loaf:
    budget -= pr_loaf
    number_of_loaves += 1
    colored_eggs += 3

    if number_of_loaves % 3 == 0:
        colored_eggs -= number_of_loaves - 2

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
