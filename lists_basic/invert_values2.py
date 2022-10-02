numbers = input().split()
opposite_numbers = []

for element in numbers:
    current_number = -int(element)
    opposite_numbers.append(current_number)
print(opposite_numbers)