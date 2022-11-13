first_symbol = input()
second_symbol = input()
text = input()
lst = []
for char in text:
    if ord(first_symbol) < ord(char) < ord(second_symbol):
        lst.append(ord(char))
print(sum(lst))
