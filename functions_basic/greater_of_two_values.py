def max_int(first, second):
    first = int(first)
    second = int(second)
    return int(max(first, second))


def max_char(first, second):
    return max(first, second)


def string_max(first, second):
    if first > second:
        return first
    return second


command = input()
first_number = input()
second_number = input()

if command == 'int':
    print(max_int(first_number, second_number))
elif command == 'char':
    print(max_char(first_number, second_number))
elif command == 'string':
    print(string_max(first_number, second_number))



