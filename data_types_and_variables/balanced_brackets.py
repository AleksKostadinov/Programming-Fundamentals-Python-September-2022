lines = int(input())
left_par = False
right_par = False
left_par_counter = 0
right_par_counter = 0
for line in range(lines):
    special_symbol = input()

    if special_symbol == '(':
        left_par = True
        left_par_counter += 1
        if left_par_counter == 2:
            left_par = False
            break
    if special_symbol == ')':
        right_par_counter += 1
        if left_par:
            right_par = True
            break

if left_par and right_par and left_par_counter == right_par_counter:
    print('BALANCED')
else:
    print('UNBALANCED')