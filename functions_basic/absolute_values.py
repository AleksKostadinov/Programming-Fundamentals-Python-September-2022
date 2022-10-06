list_numbers = input().split()
digit_list = []

for number in list_numbers:
    digit_list.append(abs(float(number)))

print(digit_list)