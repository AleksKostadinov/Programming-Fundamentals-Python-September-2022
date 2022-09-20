first_word = input()
second_word = input()
current_word = first_word
for char in range(len(second_word)):

    left_word = second_word[:char + 1]
    right_word = first_word[char+1:]
    word = left_word + right_word

    if word != current_word:
        print(word)
    current_word = word