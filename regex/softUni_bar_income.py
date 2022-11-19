import re

line = input()
name_pattern = r'%([A-Z][a-z]+)%'
product_pattern = r'<([\w]+)>'
count_pattern = r'\|(\d+)\|'
price_pattern = r'([0-9]+\.?[0-9]+)\$'
total_income = 0

while line != 'end of shift':
    match_name = ''.join(re.findall(name_pattern, line))
    match_product = ''.join(re.findall(product_pattern, line))
    match_count = ''.join(re.findall(count_pattern, line))
    match_price = ''.join(re.findall(price_pattern, line))
    if match_name and match_product and match_count and match_price:
        print(f"{match_name}: {match_product} - {(float(match_price) * int(match_count)):.2f}")
        total_income += float(match_price) * int(match_count)

    line = input()

print(f"Total income: {total_income:.2f}")
