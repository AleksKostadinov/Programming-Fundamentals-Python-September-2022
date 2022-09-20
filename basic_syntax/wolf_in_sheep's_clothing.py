word = input().split(", ")

if word[-1] == "wolf":
    print("Please go away and stop eating my sheep")

else:
    word_reversed = word[::-1]
    for i in range(len(word_reversed)):
        if word_reversed[i] == "wolf":
            print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")
