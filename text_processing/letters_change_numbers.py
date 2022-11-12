line = input().split()
result = 0
for word in line:
    first_letter = word[0]
    last_letter = word[-1]
    if first_letter.isupper():
        result += int(word[1:-1]) / (ord(first_letter) - 64)
    else:
        result += int(word[1:-1]) * (ord(first_letter) - 96)
    if last_letter.isupper():
        result -= ord(last_letter) - 64
    else:
        result += ord(last_letter) - 96
print(f'{result:.2f}')
