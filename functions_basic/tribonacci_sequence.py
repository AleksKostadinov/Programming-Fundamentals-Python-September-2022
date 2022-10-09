def tribonacci(num):
    first = 0
    second = 1
    third = 1
    if num >= 1:
        print(second, "", end="")
    if num >= 2:
        print(second, "", end="")
    for i in range(3, num + 1):
        current_number = first + second + third
        first = second
        second = third
        third = current_number
        print(current_number, "", end="")


number = int(input())
tribonacci(number)
