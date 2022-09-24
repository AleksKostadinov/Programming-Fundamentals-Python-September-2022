key = int(input())
lines = int(input())

for line in range(1, lines + 1):
    letter = input()
    ord_letter = ord(letter) + key
    print(chr(ord_letter), end='')
