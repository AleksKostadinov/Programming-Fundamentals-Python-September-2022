employee_happiness = list(map(int, input().split()))
factor = int(input())

multiplied_happiness = [employee * factor for employee in employee_happiness]

avg_happiness = (sum(employee_happiness) / len(employee_happiness)) * factor
half_employees = len(employee_happiness) // 2

happy_worker = [happy for happy in multiplied_happiness if happy >= avg_happiness]

if len(happy_worker) >= half_employees:
    print(f"Score: {len(happy_worker)}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_worker)}/{len(employee_happiness)}. Employees are not happy!")
