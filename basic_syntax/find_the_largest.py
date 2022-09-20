number = input()
number = sorted(number)
largest_number = number[::-1]

for i in largest_number:
    print(i, end='')
