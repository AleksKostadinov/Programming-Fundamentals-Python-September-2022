def header_footer(num):
    for i in range(0, (num * 2)):
        print('-', end='')
    print()


def middle(num):
    figure = '\/'
    for row in range(num - 2):
        print(f"-{figure * (num - 1)}-")


number = int(input())
header_footer(number)
middle(number)
header_footer(number)
