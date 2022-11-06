command = input()
result_dict = {}
submissions_dict = {}
while command != 'exam finished':
    command_list = command.split('-')
    if len(command_list) > 2:
        username, language, points = command_list
        if username not in result_dict:
            result_dict[username] = result_dict.get(username, 0)
        if int(points) > result_dict[username]:
            result_dict[username] = int(points)
        if language not in submissions_dict:
            submissions_dict[language] = submissions_dict.get(language, 0)
        submissions_dict[language] += 1
    else:
        username, is_banned = command_list
        del result_dict[username]
    command = input()
print('Results:')
for name, grade in result_dict.items():
    print(f"{name} | {grade}")
print('Submissions:')
for languages, number in submissions_dict.items():
    print(f'{languages} - {number}')
