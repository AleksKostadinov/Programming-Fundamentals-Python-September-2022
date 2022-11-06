contest_data = input()
contests = {}
users = {}
while contest_data != 'end of contests':
    contest, password = contest_data.split(':')
    contests[contest] = password
    contest_data = input()

submission_data = input()
while submission_data != 'end of submissions':
    contest, password, username, points = submission_data.split('=>')
    if password == contests.get(contest):
        users[username] = users.get(username, {})
        users[username][contest] = users[username].get(contest, 0)
        if users[username][contest] < int(points):
            users[username][contest] = int(points)
    submission_data = input()
candidates = {name: sum(users[name].values()) for name in users}
best_candidate = max(candidates, key=candidates.get)
print(f'Best candidate is {best_candidate} with total {candidates[best_candidate]} points.')
print('Ranking:')
for name in sorted(users):
    print(name)
    for contest, points in sorted(users[name].items(), key=lambda item: -item[1]):
        print(f"#  {contest} -> {points}")
