def triangle_area(l, h):
    area = (l * h) / 2
    if area % 1 == 0:
        return int(area)
    return area


length = float(input())
height = float(input())
print(triangle_area(length, height))
