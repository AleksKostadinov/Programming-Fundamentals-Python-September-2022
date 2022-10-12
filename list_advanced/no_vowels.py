word = input()
vowels = ['a', 'o', 'u', 'e', 'i']

list_without_vowels = [char for char in word if char.lower() not in vowels]
print(''.join(list_without_vowels))
