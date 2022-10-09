def calculate_power(number, power):
    result = number ** power
    if result % 1 == 0:
        return int(result)
    return result


first_number = float(input())
power_number = float(input())
print(calculate_power(first_number, power_number))
