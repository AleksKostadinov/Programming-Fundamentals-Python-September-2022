number = int(input())

for prime in range(2, number):
    if number % prime == 0:
        print("False")
        break
else:
    print("True")