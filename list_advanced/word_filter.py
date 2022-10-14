words_list = input().split()
text = [word for word in words_list if len(word) % 2 == 0]
print(' \n'.join(text))