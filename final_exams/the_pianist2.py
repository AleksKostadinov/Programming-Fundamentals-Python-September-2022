def add_item(piece_, composer_, key_, collection_):
    if piece_ not in collection_:
        collection[piece_] = {'composer': composer_, 'key': key_}
        return f"{piece_} by {composer_} in {key_} added to the collection!"
    return f"{piece_} is already in the collection!"


def remove_item(piece_, collection_):
    if piece_ in collection_:
        del collection_[piece_]
        return f"Successfully removed {piece_}!"
    return f"Invalid operation! {piece_} does not exist in the collection."


def change_key(piece_, new_key_, collection_):
    if piece_ in collection_:
        collection_[piece_]['key'] = new_key_
        return f"Changed the key of {piece_} to {new_key_}!"
    return f"Invalid operation! {piece_} does not exist in the collection."


number_of_pieces = int(input())

collection = {}
for number in range(number_of_pieces):
    pieces, composer, key = input().split('|')
    collection[pieces] = {'composer': composer, 'key': key}
command = input()
while command != 'Stop':
    action, *other = command.split('|')
    if action == 'Add':
        piece, composer, key = other[0], other[1], other[2],
        print(add_item(piece, composer, key, collection))
    elif action == 'Remove':
        piece = other[0]
        print(remove_item(piece, collection))
    elif action == 'ChangeKey':
        piece, new_key = other[0], other[1]
        print(change_key(piece, new_key, collection))
    command = input()
for pieces, info in collection.items():
    print(f"{pieces} -> Composer: {info['composer']}, Key: {info['key']}")
