word = input()
last_letter = word[-1:]
last_letter2 = word[-1:]
last_letters = word[-2:]
my_list1 = ['y']
my_list2 = ['ch', 'sh', 'o', 's', 'x', 'z']
if last_letter in my_list1:
    word = word[:-1] + 'ies'
    print(word)
elif last_letter2 in my_list2:
    word += 'es'
    print(word)
elif last_letters in my_list2:
    word += 'es'
    print(word)
else:
    word += 's'
    print(word)
