import math


def is_prime(n, primes):
    max_value = int(math.sqrt(n)) + 1

    for p in primes:
        if p < max_value and n % p == 0:
            return False
    return True


def get_primes_below(n, known_primes):
    primes = known_primes
    biggest_prime = max(primes)
    for i in range(biggest_prime, n, 2):
        if is_prime(i, primes):
            primes.add(i)
    return primes


def solve():
    primes = {2, 3}

    curr = 1
    step = 2

    diagonal_primes = 0
    total = 1
    while True:
        primes = get_primes_below(
            int(math.sqrt(curr + step * 4)) + 1,
            primes
        )

        for i in range(4):
            curr += step
            if is_prime(curr, primes):
                diagonal_primes += 1

        total += 4
        r = float(diagonal_primes) / total

        if r < 0.1:
            return step + 1

        step += 2

print(solve())
