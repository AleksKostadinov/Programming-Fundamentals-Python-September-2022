from math import floor


def coordinate(fst, snd, trd, fth):
    fst_pair = fst ** 2 + snd ** 2
    snd_pair = trd ** 2 + fth ** 2
    if fst_pair > snd_pair:
        return f"({trd}, {fth})"
    else:
        return f"({fst}, {snd})"


x1 = floor(float(input()))
y1 = floor(float(input()))
x2 = floor(float(input()))
y2 = floor(float(input()))
print(coordinate(x1, y1, x2, y2))
