count = 0
while True:
    try:
        number = int(input())
        count += 1
    except:
        print(count)
        break