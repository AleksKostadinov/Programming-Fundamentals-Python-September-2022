first_string, second_string = input().split()
result = 0
if len(first_string) > len(second_string):
    for i in range(len(second_string)):
        result += ord(first_string[i]) * ord(second_string[i])
    for i in range(len(second_string), len(first_string)):
        result += ord(first_string[i])
else:
    for i in range(len(first_string)):
        result += ord(first_string[i]) * ord(second_string[i])
    for i in range(len(first_string), len(second_string)):
        result += ord(second_string[i])
print(result)