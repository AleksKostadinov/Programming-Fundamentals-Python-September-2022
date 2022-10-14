def electrons_in_shell(electron):
    max_electrons_in_shell = 2 * electron ** 2
    return max_electrons_in_shell


def shells(number_electrons):
    list_electrons = []
    for i in range(1, number_electrons + 1):
        electrons_to_add = electrons_in_shell(i)
        if electrons_to_add >= number_electrons:
            list_electrons.append(number_electrons)
            break
        number_electrons -= electrons_to_add
        list_electrons.append(electrons_to_add)
    return list_electrons


electrons = int(input())
print(shells(electrons))
