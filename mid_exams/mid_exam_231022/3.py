price_ratings = list(map(int, input().split(', ')))
entry_point = int(input())
type_of_items = input()
value_entry = price_ratings[entry_point]
left_total = 0
right_total = 0
position = ''
left_side = price_ratings[:entry_point]
right_side = price_ratings[entry_point + 1:]
if type_of_items == 'cheap':
    if entry_point in range(len(price_ratings)):
        for left in left_side:
            if left < value_entry:
                left_total += left
                position = 'Left'
        for right in right_side:
            if right < value_entry:
                right_total += right
                position = 'Right'
else:
    if entry_point in range(len(price_ratings)):
        for left in left_side:
            if left >= value_entry:
                left_total += left
                position = 'Left'
        for right in right_side:
            if right >= value_entry:
                right_total += right
                position = 'Right'

if left_total >= right_total:
    print(f"Left - {left_total}")
else:
    print(f"{position} - {right_total}")