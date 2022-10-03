list_numbers = input().split()
length = len(list_numbers)
mid = length // 2
left_sum = 0
right_sum = 0

for left in range(mid):
    left_sum += int(list_numbers[left])
    if list_numbers[left] == '0':
        left_sum *= 0.8
for right in range(length - 1, mid, -1):
    right_sum += int(list_numbers[right])
    if list_numbers[right] == '0':
        right_sum *= 0.8

if left_sum > right_sum:
    winner_side = right_sum
    winner = 'right'
else:
    winner_side = left_sum
    winner = 'left'

print(f'The winner is {winner} with total time: {winner_side:.1f}')