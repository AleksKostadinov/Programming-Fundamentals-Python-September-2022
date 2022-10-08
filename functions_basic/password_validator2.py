def valid_password(some_password):
    validation = []
    digit_counter = 0
    if len(some_password) < 6 or 10 < len(some_password):
        validation.append("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        is_valid = False
        validation.append("Password must consist only of letters and digits")
    for char in some_password:
        if char.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        validation.append("Password must have at least 2 digits")
    return validation


password = input()
not_valid_password = valid_password(password)

if not_valid_password:
    print('\n'.join(not_valid_password))
else:
    print("Password is valid")