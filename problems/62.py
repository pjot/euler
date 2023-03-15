from collections import Counter


def solve():
    cubes = Counter()
    smallest = {}
    n = 0

    while True:
        n += 1
        cube = n * n * n
        key = "".join(sorted(str(cube)))

        cubes[key] += 1
        smallest[key] = min(
            smallest.get(key, float("inf")),
            cube
        )

        most_common, count = cubes.most_common()[0]
        if count == 5:
            return smallest[most_common]


print(solve())
