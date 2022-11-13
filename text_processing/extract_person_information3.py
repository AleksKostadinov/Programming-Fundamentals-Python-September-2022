number_lines = int(input())

for line in range(number_lines):
    lines = input()
    name = lines[lines.index("@") + 1:lines.index("|")]
    age = lines[lines.index("#") + 1:lines.index("*")]
    print(f"{name} is {age} years old.")
