fires_cells_list = input().split('#')
current_water = int(input())
fire_cells = []
effort = 0

for cell in fires_cells_list:
    is_valid = False
    list_with_cells = cell.split()
    water_needed = int(list_with_cells[2])
    if current_water >= water_needed:
        if 'High' in list_with_cells and 81 <= water_needed <= 125 or \
                'Medium' in list_with_cells and 51 <= water_needed <= 80 or \
                'Low' in list_with_cells and 1 <= water_needed <= 50:
            is_valid = True
    if is_valid:
        fire_cells.append(water_needed)
        effort += water_needed * 0.25
        current_water -= water_needed

print('Cells:')
for cell in fire_cells:
    print(f' - {cell}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(fire_cells)}')
