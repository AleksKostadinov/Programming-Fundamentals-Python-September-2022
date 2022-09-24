snowballs = int(input())
max_snowball_value = 0
best_snowball_quality = 0
best_snowball_weight = 0
best_snowball_time = 0
for snowball in range(snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / snowball_time) ** snowball_quality

    if snowball_value > max_snowball_value:
        best_snowball_weight = snowball_weight
        best_snowball_time = snowball_time
        max_snowball_value = snowball_value
        best_snowball_quality = snowball_quality

print(f"{best_snowball_weight} : {best_snowball_time} = {int(max_snowball_value)} ({best_snowball_quality})")