year = int(input())
is_not_happy_year = True

while is_not_happy_year:
    year += 1
    year_set = set()
    for i in range(len(str(year))):
        year_set.add(str(year)[i])
    is_not_happy_year = len(year_set) != len(str(year))

print(year)
