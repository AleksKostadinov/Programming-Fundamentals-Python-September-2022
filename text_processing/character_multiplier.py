first_string, second_string = input().split()
first = [ord(x) for x in first_string]
second = [ord(x) for x in second_string]
multiply = 0
if len(first_string) > len(second_string):
    for i in range(len(second_string)):
        multiply += first[i] * second[i]
    for i in range(len(second_string), len(first_string)):
        multiply += first[i]
else:
    for j in range(len(first_string)):
        multiply += first[j] * second[j]
    for j in range(len(first_string), len(second_string)):
        multiply += second[j]
print(multiply)
