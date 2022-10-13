def palindrome_filtered(word):
    if word == word[::-1]:
        return word


words = input().split()
palindrome = input()

palindrome_list = [word for word in words if palindrome_filtered(word)]
counter = palindrome_list.count(palindrome)
print(palindrome_list)
print(f'Found palindrome {counter} times')
