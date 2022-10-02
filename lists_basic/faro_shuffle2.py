cards = input().split()
shuffles = int(input())
length = len(cards)
mid = int(length / 2)
left_side = []
right_side = []

for shuffle in range(shuffles):
    final_deck = []
    for element in range(mid):
        left_side = cards[0:mid]
        right_side = cards[mid:]
        final_deck.append(left_side[element])
        final_deck.append(right_side[element])
    cards = final_deck
print(cards)

