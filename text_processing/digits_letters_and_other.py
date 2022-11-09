word = input()
digit, string, others = [], [], []

for char in word:
    if char.isdigit():
        digit.append(char)
    elif char.isalpha():
        string.append(char)
    else:
        others.append(char)
print(f"{''.join(digit)}\n{''.join(string)}\n{''.join(others)}")
