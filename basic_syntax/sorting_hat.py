names = input()
char = 0

while names != "Welcome!":
    char = len(names)
    if names != "Voldemort":
        if char < 5:
            print(f"{names} goes to Gryffindor.")
        elif char == 5:
            print(f"{names} goes to Slytherin.")
        elif char == 6:
            print(f"{names} goes to Ravenclaw.")
        elif char > 6:
            print(f"{names} goes to Hufflepuff.")
    else:
        print("You must not speak of that name!")
        break
    names = input()
else:
    print("Welcome to Hogwarts.")