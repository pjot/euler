fac = {
    0: 1,
    1: 1,
    2: 2,
    3: 6,
    4: 24,
    5: 120,
    6: 720,
    7: 5040,
    8: 40320,
    9: 362880,
}


def factorial_sum(n):
    digits = [int(i) for i in str(n)]
    return sum(fac[d] for d in digits)


def solve():
    cache = {}
    for i in range(1, 1000000):
        seen = set()
        steps = 0
        n = i
        while True:
            if n in cache:
                cache[i] = cache[n] + steps
                break

            if n in seen:
                cache[i] = steps
                break

            seen.add(n)
            steps += 1
            n = factorial_sum(n)


    return len([v for v in cache.values() if v == 60])


print(solve())
