first_symbol, second_symbol, text = input(), input(), input()

print(sum(ord(char) for char in text if ord(first_symbol) < ord(char) < ord(second_symbol)))
