employee_happiness = list(map(int, input().split()))
factor = int(input())
multiplied_happiness = []
happy_worker = []

for employee in employee_happiness:
    result = employee * factor
    multiplied_happiness.append(result)

avg_happiness = (sum(employee_happiness) / len(employee_happiness)) * factor
for happy in multiplied_happiness:
    if happy >= avg_happiness:
        happy_worker.append(happy)

half_employees = len(employee_happiness) // 2

if len(happy_worker) >= half_employees:
    print(f"Score: {len(happy_worker)}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_worker)}/{len(employee_happiness)}. Employees are not happy!")