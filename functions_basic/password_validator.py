def valid_password(some_password):
    is_valid = True
    digit = 0
    length = len(some_password)
    if length < 6 or length > 10:
        is_valid = False
        print(f'Password must be between 6 and 10 characters')
    if not some_password.isalnum():
        is_valid = False
        print(f"Password must consist only of letters and digits")
    for char in some_password:
        if char.isdigit():
            digit += 1
    if digit < 2:
        is_valid = False
        print(f'Password must have at least 2 digits')
    if is_valid:
        print(f'Password is valid')


password = input()
valid_password(password)
