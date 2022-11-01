country = input().split(', ')
capitals = input().split(', ')

result = dict(zip(country, capitals))
[print(f'{k} -> {v}') for k, v in result.items()]
# [print(f'{countries} -> {result[countries]}') for countries in result]