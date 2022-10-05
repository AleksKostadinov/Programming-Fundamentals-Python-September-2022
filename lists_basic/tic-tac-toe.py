def winner(one, two, three):
    if "1" == one[0] == one[1] == one[2] or "1" == two[0] == two[1] == two[2] \
            or "1" == three[0] == three[1] == three[2]:  # horizontal
        return "First player won"
    elif "1" == one[0] == two[0] == three[0] or "1" == one[1] == two[1] == three[1] \
            or "1" == one[2] == two[2] == three[2]:  # vertical
        return "First player won"
    elif "1" == one[0] == two[1] == three[2] or "1" == one[2] == two[1] == three[0]:  # diagonal
        return "First player won"
    elif "2" == one[0] == one[1] == one[2] or "2" == two[0] == two[1] == two[2] \
            or "2" == three[0] == three[1] == three[2]:  # horizontal
        return "Second player won"
    elif "2" == one[0] == two[0] == three[0] or "2" == one[1] == two[1] == three[1] \
            or "2" == one[2] == two[2] == three[2]:  # vertical
        return "Second player won"
    elif "2" == one[0] == two[1] == three[2] or "2" == one[2] == two[1] == three[0]:  # diagonal
        return "Second player won"
    else:
        return "Draw!"


first_row = input().split()
second_row = input().split()
third_row = input().split()

result = winner(first_row, second_row, third_row)
print(result)
