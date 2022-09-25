character = input()

if character.isdigit():
    print('digit')
elif character in 'aeoui':
    print('vowel')
else:
    print('other')