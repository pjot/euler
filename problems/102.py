class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

def contains_origin(a, b, c):
    j = sign(Point(0, 0), a, b) < 0
    k = sign(Point(0, 0), b, c) < 0
    l = sign(Point(0, 0), c, a) < 0
    return j == k == l

def sign(a, b, c):
    return (a.x - c.x) * (b.y - c.y) - (b.x - c.x) * (a.y - c.y)

contains = 0
with open("problems/102.txt") as f:
    for line in f:
        a_x, a_y, b_x, b_y, c_x, c_y = (int(i) for i in line.rstrip().split(","))
        a = Point(a_x, a_y)
        b = Point(b_x, b_y)
        c = Point(c_x, c_y)
        if contains_origin(a, b, c):
            contains += 1

print("Triangles containing origin: {}".format(contains))
