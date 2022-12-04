people = int(input())
lift = list(map(int, input().split(" ")))
index = 0

while people > 0:
    if index < len(lift):
        needed = 4 - lift[index]
        if people >= needed:
            lift[index] = lift[index] + needed
            people = people - needed
        else:
            lift[index] = lift[index] + people
            people = 0
    else:
        break
    index += 1

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif len([cart for cart in lift if cart < 4]) > 0:
    print('The lift has empty spots!')
print(" ".join(list(map(str, lift))))
