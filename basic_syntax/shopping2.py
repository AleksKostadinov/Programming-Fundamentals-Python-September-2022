budget = int(input())
command = input()

while command != "End":
    bought = int(command)
    budget -= bought
    if budget < 0:
        print(f"You went in overdraft!")
        break

    command = input()
else:
    print(f"You bought everything needed.")