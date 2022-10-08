def positive_integers(number):
    if number == number[::-1]:
        return True
    return False


list_of_numbers = input().split(', ')

for element in list_of_numbers:
    print(positive_integers(element))
