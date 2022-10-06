list_numbers = list(map(float, input().split()))

result = [abs(num) for num in list_numbers]

print(result)