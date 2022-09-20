text = input().lower()
my_list = ["sand", "water", "fish", "sun"]
count = 0
for i in my_list:
    if i in text:
        total_count = text.count(i)
        count += total_count
print(count)
