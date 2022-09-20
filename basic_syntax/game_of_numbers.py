first = int(input())
second = int(input())
magical = int(input())
count = 0
is_found = False
for i in range(first, second + 1):
    for j in range(first, second + 1):
        count += 1
        if i + j == magical:
            print(f"Number found! {j} + {i} = {magical}")
            is_found = True
            break
        if is_found:
            break
    if is_found:
        break

if not is_found:
    print(f"{count} combinations - neither equals {magical}")