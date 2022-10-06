grade_score = float(input())


def grade_func(grade):
    if 2.00 <= grade <= 2.99:
        return 'Fail'
    elif grade <= 3.49:
        return 'Poor'
    elif grade <= 4.49:
        return 'Good'
    elif grade <= 5.49:
        return 'Very Good'
    elif grade <= 6.00:
        return 'Excellent'


print(grade_func(grade_score))
