lines = int(input())
list_of_positive = []
list_of_negative = []

for line in range(lines):
    numbers = int(input())
    if numbers >= 0:
        list_of_positive.append(numbers)
    else:
        list_of_negative.append(numbers)

print(list_of_positive)
print(list_of_negative)
print(f'Count of positives: {len(list_of_positive)}')
print(f'Sum of negatives: {sum(list_of_negative)}')
