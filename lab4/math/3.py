import math

def polygon_area(n, s):
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return area

num_sides = int(input())
side_length = int(input())
area = polygon_area(num_sides, side_length)
print(area)
