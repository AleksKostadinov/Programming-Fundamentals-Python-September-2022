def max_min_sum(numbers):
    max_number = max(numbers)
    min_number = min(numbers)
    sum_numbers = sum(numbers)
    return f'The minimum number is {min_number}\nThe maximum number is {max_number}\nThe sum number is: {sum_numbers}'  
    
   
list_of_numbers = [int(x) for x in input().split()]
print(max_min_sum(list_of_numbers))
