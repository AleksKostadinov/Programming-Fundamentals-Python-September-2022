number = int(input())

for char1 in range(97, 97 + number):
    for char2 in range(97, 97 + number):
        for char3 in range(97, 97 + number):
            word = chr(char1) + chr(char2) + chr(char3)
            print(word)
