words = input().split()
palindrome = input()

palindrome_list = [word for word in words if word == word[::-1]]
count = palindrome_list.count(palindrome)
print(palindrome_list)
print(f'Found palindrome {count} times')