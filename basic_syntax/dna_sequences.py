num = int(input())
dna = 'ACGT'
points = 0
count = 0
for a in dna:
    for b in dna:
        for c in dna:
            for_word = a + b + c
            for i in for_word:
                if i == 'A':
                    points += 1
                elif i == 'C':
                    points += 2
                elif i == 'G':
                    points += 3
                elif i == 'T':
                    points += 4
            if points >= num:
                special_char = "O"
            else:
                special_char = "X"
            word = f'{special_char}{a}{b}{c}{special_char}'
            points = 0
            print(word, end=' ')
            count += 1
            if count % 4 == 0:
                print()
