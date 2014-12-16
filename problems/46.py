import prime
import math

def get_odd_composites():
    prime_gen = prime.Prime()
    prime_gen.next()
    prime_gen.next()
    prime_gen.next()
    c = 7
    next_prime = 0
    while True:
        last_prime, next_prime = next_prime, prime_gen.next()
        while c < next_prime:
            if c == last_prime:
                last_prime, next_prime = next_prime, prime_gen.next()
            c += 2
            if c != last_prime:
                yield c

def has_property(number):
    for p in prime.get_primes_below(number):
        for n in range(number):
            result = p + 2 * n ** 2
            if result > number:
                break
            if result == number:
                return True
    return False

for number in get_odd_composites():
    if not has_property(number):
        print("Smallest odd composite: {}".format(number))
        exit()
