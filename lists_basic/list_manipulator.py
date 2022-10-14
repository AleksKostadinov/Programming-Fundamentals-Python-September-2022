numbers = [int(number) for number in input().split()]


def exchange(index):
    global numbers
    if 0 <= index < len(numbers):
        numbers = numbers[index + 1:] + numbers[:index + 1]
    else:
        print("Invalid index")


def min_max(min_max, even_odd):
    global even, odd
    if min_max == "max":
        if even_odd == "even" and even:
            print((len(numbers) - 1) - numbers[::-1].index(max(even)))
        elif even_odd == "odd" and odd:
            print((len(numbers) - 1) - numbers[::-1].index(max(odd)))
        else:
            print("No matches")
    elif min_max == "min":
        if even_odd == "even" and even:
            print((len(numbers) - 1) - numbers[::-1].index(min(even)))
        elif even_odd == "odd" and odd:
            print((len(numbers) - 1) - numbers[::-1].index(min(odd)))
        else:
            print("No matches")


def first_last_numbers(first_last, count_of_numbers, even_odd):
    global even, odd
    if 0 <= count_of_numbers <= len(numbers):
        if first_last == "first" and even_odd == "even":
            print(even[:count_of_numbers])
        elif first_last == "first" and even_odd == "odd":
            print(odd[:count_of_numbers])
        elif first_last == "last" and even_odd == "even":
            print(even[-count_of_numbers:])
        elif first_last == "last" and even_odd == "odd":
            print(odd[-count_of_numbers:])
    else:
        print("Invalid count")


command = input()
while command != "end":
    even = [number for number in numbers if number % 2 == 0]
    odd = [number for number in numbers if number % 2 != 0]
    command = command.split()
    command_type = command[0]
    if command_type == "exchange":
        index = int(command[1])
        exchange(index)
    elif command_type == "max" or command_type == "min":
        min_max(command[0], command[1])
    elif command_type == "first" or command_type == "last":
        first_last_numbers(command[0], int(command[1]), command[2])
    command = input()

print(numbers)

# https://github.com/kumchovylcho/softuni/blob/master/Fundamentals%20-%20Python/Lists_Basics%20-%20more%20exercises/List_manipulator.py