numbers = [int(x) for x in input().split()]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)
