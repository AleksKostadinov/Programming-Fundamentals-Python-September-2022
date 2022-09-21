year = int(input())

while True:
    year += 1
    my_list = []
    for i in str(year):
        if i in str(my_list):
            year = int(year)
            break
        my_list.append(i)
    if len(my_list) == len(str(year)):
        print(year)
        break
