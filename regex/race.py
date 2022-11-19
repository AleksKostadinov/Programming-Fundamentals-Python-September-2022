import re

names = input().split(', ')
line = input()
race_dict = {}
sorted_list = []
pattern_name = r'[^\W\d]+'
pattern_numbers = r'[\d]'

while line != 'end of race':
    matches_names = ''.join(re.findall(pattern_name, line))
    str_represented_numbers = re.findall(pattern_numbers, line)
    matches_numbers = sum([int(x) for x in str_represented_numbers])
    if matches_names in names:
        if matches_names not in race_dict:
            race_dict[matches_names] = 0
        race_dict[matches_names] += matches_numbers
    line = input()

sorted_list = sorted(race_dict.items(), key=lambda x: x[1], reverse=True)

print(f'1st place: {sorted_list[0][0]}')
print(f'2nd place: {sorted_list[1][0]}')
print(f'3rd place: {sorted_list[2][0]}')
