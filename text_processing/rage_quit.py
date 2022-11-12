word = input().upper()
result, letters, number = '', '', ''

for index, char in enumerate(word):
    if not char.isdigit():
        letters += char
    else:
        for next_symbol in word[index::]:
            if next_symbol.isdigit():
                number += next_symbol
            else:
                break
        result += letters * int(number)
        letters, number = '', ''
print(f'Unique symbols used: {len(set(result))}')
print(result)
