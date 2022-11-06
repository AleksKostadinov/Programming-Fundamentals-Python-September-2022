command = input()
company_dict = {}
while command != 'End':
    company_name, employee_id = command.split(' -> ')
    if company_name not in company_dict:
        company_dict[company_name] = []
    if employee_id not in company_dict[company_name]:
        company_dict[company_name].append(employee_id)
    command = input()
for company_name, employee_id in company_dict.items():
    print(company_name)
    for employee in employee_id:  # for i in range(len(employee_id)):
        print(f'-- {employee}')  # print(f'-- {employee_id[i]}')
