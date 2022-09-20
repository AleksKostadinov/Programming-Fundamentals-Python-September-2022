first = input()
second = input()
third = input()

for i in range(ord(first), ord(second) + 1):
    if chr(i) == third:
        continue
    for j in range(ord(first), ord(second) + 1):
        if chr(j) == third:
            continue
        for k in range(ord(first), ord(second) + 1):
            if chr(k) == third:
                continue
            word = chr(i) + chr(j) + chr(k)
            print(word, end=' ')
