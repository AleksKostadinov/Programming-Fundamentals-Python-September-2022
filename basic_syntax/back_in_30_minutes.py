hours = int(input())
minutes = int(input())

minutes += 30
if minutes > 60:
    minutes = minutes - 60
    hours += 1
if hours > 23:
    hours = 0
print(f'{hours}:{minutes:02d}')
