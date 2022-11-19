import re

line = input()
pattern = r'%([A-Z][a-z]+)%[^\|\$\%\.]*<(\w+)>[^\|\$\%\.]*\|(\d+)\|[^\|\$\%\.\d]*(((\d+)(\.)?\d+)*)\$'
# name_pattern = r'%([A-Z][a-z]+)%'
# product_pattern = r'<([\w]+)>'
# count_pattern = r'\|(\d+)\|'
# price_pattern = r'([0-9]+\.?[0-9]+)\$'
total_income = 0

while line != 'end of shift':
    match = re.search(pattern, line)
    if match:
        match_name = match.group(1)
        match_product = match.group(2)
        match_price = int(match.group(3))
        match_count = float(match.group(4))

        income = match_price * match_count
        print(f"{match_name}: {match_product} - {income:.2f}")
        total_income += income

    line = input()
print(f"Total income: {total_income:.2f}")
