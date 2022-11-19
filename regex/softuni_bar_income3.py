import re

line = input()

pattern = re.compile(
    r"(%)(?P<customer>[A-Z][a-z]+)\1([^\|\$\%\.]*)"
    r"<(?P<product>[\w]+)>([^\|\$\%\.]*)"
    r"\|(?P<count>[\d]+)\|([^\|\$\%\.]*)"
    r"(?P<price>[1-9]+[.0-9]*)\$"
)

total_income = 0

while line != 'end of shift':
    result = re.finditer(pattern, line)

    for show in result:
        income = int(show['count']) * float(show['price'])
        print(f"{show['customer']}: {show['product']} - {income:.2f}")
        total_income += income

    line = input()
print(f"Total income: {total_income:.2f}")
