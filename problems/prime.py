import math

# Prime number generator
class Prime():
    def __init__(self):
        self.primes = [2, 3]
        self.current_number = 2

    # Get the next prime number
    def next(self):
        if self.current_number == 2:
            self.current_number = 1
            return 2

        self.current_number = self.current_number + 2

        while not self.is_prime(self.current_number):
            self.current_number = self.current_number + 2

        self.primes.append(self.current_number)
        return self.current_number

    def is_prime(self, number):
        for prime in self.primes:
            if prime > math.sqrt(number):
                return True
            if number % prime == 0:
                return False
        return True

# Calculates if a number n is a prime or not
def is_prime(n):
    if n == 2:
        return True

    if n < 2:
        return False

    if n % 2 == 0:
        return False

    # We only have to check up to sqrt(n)
    max_value = int(math.sqrt(n))
    for i in range(3, max_value, 2):
        if n % i == 0:
            return False

    return True

# Returns all primes below n
def get_primes_below(n):
    primes = []
    for i in range(n):
        if is_prime(i):
            yield i

# Returns all unique prime factors of n
def get_factors(n):
    factors = []
    for prime in get_primes_below(n):
        if n % prime == 0:
            yield prime
            n = n / prime
            if n < prime:
                return

def get_proper_factors(n):
    factors = set()
    for factor in range(1, int(math.sqrt(n)) + 1):
        if n % factor == 0:
            factors.add(factor)
            if factor != 1 and n != factor:
                factors.add(int(n / factor))
    return factors

def get_all_factors(n):
    factors = get_proper_factors(n)
    factors.add(n)
    return factors
