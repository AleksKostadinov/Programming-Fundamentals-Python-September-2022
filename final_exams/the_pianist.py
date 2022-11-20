number_of_pieces = int(input())

pieces_dict = {}

for number in range(number_of_pieces):
    piece, author, key = input().split('|')
    if piece not in pieces_dict:
        pieces_dict[piece] = {author: 0}
    pieces_dict[piece][author] = key

command = input()
while command != 'Stop':
    command = command.split('|')
    action = command[0]
    piece = command[1]
    if action == 'Add':
        author, key = command[2], command[3]
        if piece not in pieces_dict:
            pieces_dict[piece] = {author: key}
            print(f"{piece} by {author} in {key} added to the collection!")
        else:
            print(f'{piece} is already in the collection!')
    elif action == 'Remove':
        if piece not in pieces_dict:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            del pieces_dict[piece]
            print(f"Successfully removed {piece}!")
    elif action == 'ChangeKey':
        new_key = command[2]
        if piece not in pieces_dict:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            for current_piece in pieces_dict:
                if current_piece == piece:
                    for (compositor) in pieces_dict[current_piece]:
                        pieces_dict[current_piece][compositor] = new_key
                        break
            print(f"Changed the key of {piece} to {new_key}!")
    command = input()
for piece_, values in pieces_dict.items():
    for composer, keys in values.items():
        print(f'{piece_} -> Composer: {composer}, Key: {keys}')
