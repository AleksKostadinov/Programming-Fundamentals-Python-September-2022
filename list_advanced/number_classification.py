number_list = input().split(', ')

filtered_positive = [num for num in number_list if int(num) >= 0] 
filtered_negative = [num for num in number_list if int(num) < 0] 
filtered_even = [num for num in number_list if int(num) % 2 == 0]
filtered_odd = [num for num in number_list if int(num) % 2 != 0]

print(f"Positive: {', '.join(filtered_positive)}")
print(f"Negative: {', '.join(filtered_negative)}")
print(f"Even: {', '.join(filtered_even)}")
print(f"Odd: {', '.join(filtered_odd)}")