def positive_integers(numbers):
    for number in numbers:
        if number == number[::-1]:
            print('True')
        else:
            print('False')
    

list_of_numbers = input().split(', ')
positive_integers(list_of_numbers)
