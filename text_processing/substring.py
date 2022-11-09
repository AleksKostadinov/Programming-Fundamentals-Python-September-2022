magic_word = input()
word = input()
while magic_word in word:
   word = word.replace(magic_word, '')
print(word)
