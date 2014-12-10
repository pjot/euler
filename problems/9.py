for a in range(1, 1000):
    for b in range(a, 1000):
        c = 1000 - a - b
        if a * a + b * b == c * c:
            print("Product of triplet a = {}, b = {}, c = {}: {}".format(a, b, c, a * b * c))
            exit()
