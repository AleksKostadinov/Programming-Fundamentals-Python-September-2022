divisor = int(input())
boundary = int(input())
num = 0
for num in range(boundary, 0, - 1):
    if num % divisor == 0:
        break
print(num)
