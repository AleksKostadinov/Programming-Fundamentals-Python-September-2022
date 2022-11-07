command = input()
courses, individual = {}, {}
while command != 'no more time':
    username, contest, points = command.split(' -> ')
    courses[contest] = courses.get(contest, {})
    courses[contest][username] = courses[contest].get(username, 0)
    if courses[contest][username] < int(points):
        courses[contest][username] = int(points)
    command = input()

for course in courses:
    print(f'{course}: {len(courses[course])} participants')
    for pos, (username, points) in enumerate(sorted(courses[course].items(), key=lambda x: (-x[1], x[0])), 1):
        print(f"{pos}. {username} <::> {points}")
        individual[username] = individual.get(username, 0) + points
print("Individual standings:")
for pos, (username, points) in enumerate(sorted(individual.items(), key=lambda x: (-x[1], x[0])), 1):
    print(f'{pos}. {username} -> {points}')
