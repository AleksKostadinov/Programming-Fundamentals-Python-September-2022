electrons = int(input())
list_electrons = []
for electron in range(1, electrons + 1):
    max_num_electrons = 2 * electron ** 2
    if max_num_electrons >= electrons:
        list_electrons.append(electrons)
        break
    electrons -= max_num_electrons
    list_electrons.append(max_num_electrons)

print(list_electrons)
