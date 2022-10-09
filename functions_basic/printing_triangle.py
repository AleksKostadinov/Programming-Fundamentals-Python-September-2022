def triangle_figure(num):
    for row in range(1, num + 1):
        for col in range(1, row + 1):
            print(col, end=' ')
        print()
    for reverse_row in range(num):
        for reverse_col in range(num - reverse_row - 1):
            print(reverse_col + 1, end=' ')
        print()


number = int(input())
triangle_figure(number)
