number_cities = int(input())
total_profit = 0
for city in range(1, number_cities + 1):
    name_city = input()
    money_earned = float(input())
    expenses = float(input())
    if city % 5 == 0:
        money_earned *= 0.9
    elif city % 3 == 0:
        expenses *= 1.5
    profit = money_earned - expenses
    total_profit += profit
    print(f"In {name_city} Burger Bus earned {profit:.2f} leva.")
print(f"Burger Bus total profit: {total_profit:.2f} leva.")